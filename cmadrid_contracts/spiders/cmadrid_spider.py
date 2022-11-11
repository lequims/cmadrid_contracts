import scrapy
from cmadrid_contracts.items import ContractItem
from scrapy.selector import Selector 

class Cmadrid_Spider(scrapy.Spider):
    
    # name of variable should be 'name' only
    name = "cmadrid" 
    
    # urls from which will be used to extract information
    # list should be named 'start_urls' only
    #start_urls = ["https://www.madrid.org/cs/Satellite?c=Page&cid=1224915242285&codigo=PCON_&idPagina=1224915242285&language=es&newPagina=1&numPagListado=5&pagename=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&paginaActual=2&paginasTotal=341616&rootelement=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&site=PortalContratacion"]
    start_urls = ["http://www.madrid.org/cs/Satellite?c=Page&cid=1224915242285&codigo=PCON_&idPagina=1224915242285&language=es&newPagina=1&numPagListado=5&pagename=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&paginaActual=2&paginasTotal=1204&rootelement=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&site=PortalContratacion&tipoPublicacion=Contratos+adjudicados+por+procedimientos+sin+publicidad"]
    base_url = 'https://www.madrid.org/'

    def parse(self, response):

        all_contracts_in_page =  response.xpath('//div[contains(@class, "cajaBlanca")]/div[contains(@class, "cajaBlancaDosL")]')
        
        # Extrating link to every contract
        sel = Selector(response)
        page = sel.xpath('//div[contains(@class, "caja")]/ul/li/a[contains (@class, "activo")]/text()').get()
       
        for contract in all_contracts_in_page:
            
            contract_url = contract.xpath('.//a/@href').extract_first()
            yield scrapy.Request(self.base_url + contract_url, callback=self.parse_contract, meta={'page': page})

        next_page = response.xpath('//div[contains(@id, "pagSup")]/div[contains(@class, "caja")]/ul/li/a[contains (@class, "activo")]/following::li/a/@href').get()

        #yield scrapy.Request("https://www.madrid.org//cs/Satellite?c=CM_ConvocaPrestac_FA&cid=1354931493274&definicion=Contratos+Publicos&idPagina=1224915242285&language=es&op2=PCON&pagename=PortalContratacion%2FPage%2FPCON_contratosPublicos&tipoServicio=CM_ConvocaPrestac_FA", callback=self.parse_contract, meta={'page': page})

        
        if next_page:
            yield scrapy.Request(
                url = self.base_url + next_page,
                callback = self.parse
            ) 
        
    def parse_contract(self, response):
        
        # treatment of all fields
        fields = response.xpath('//li[contains(@class, "txt08gr3")]')

        data_fields = {}
        
        for field in fields:
            field_name = field.xpath('.//strong/text()').extract_first()
            value = field.xpath('.//strong/following::br/following::text()').extract_first()
            
            if(field_name):
                data_fields[field_name] = value   

        contract_item = ContractItem(
            
            Objeto_del_contrato = response.xpath('//h2[contains(@class, "tit11gr3")]/text()').extract_first(),
            plazo = response.xpath('//div[contains(@id, "cont_int_izdo")]/span/text()').extract_first(),
            url = response.url,
            Estado_de_la_licitación = data_fields.get('Estado de la licitación',None),
            Tipo_resolución = data_fields.get('Tipo resolución',None),
            Tipo_Publicación = data_fields.get('Tipo Publicación',None),
            Código_CPV = data_fields.get('Código CPV',None),
            Compra_pública_innovadora = data_fields.get('Compra pública innovadora',None),
            Número_de_expediente = data_fields.get('Número de expediente',None),
            Referencia = data_fields.get('Referencia',None),
            Tipo_de_contrato = data_fields.get('Tipo de contrato',None),
            Entidad_adjudicadora = data_fields.get('Entidad adjudicadora',None),
            Procedimiento_Adjudicación = data_fields.get('Procedimiento Adjudicación',None),
            Valor_estimado_sin_IVA = data_fields.get('Valor estimado sin I.V.A',None),
            Presupuesto_base_licitación_sin_impuestos = data_fields.get('Presupuesto base licitación (sin impuestos)',None),
            Duración_del_contrato = data_fields.get('Duración del contrato',None),
            Presupuesto_base_licitación_Importe_total = data_fields.get('Presupuesto base licitación. Importe total',None),
            Puntos_de_Información = data_fields.get('Puntos de Información',None),
            Adjudicación_del_contrato_publicada_el = data_fields.get('Adjudicación del contrato publicada el',None),
            Formalización_del_contrato_publicada_el = data_fields.get('Formalización del contrato publicada el',None),
            Formalización_del_contrato_publicada_en_BOCM_el = data_fields.get('Formalización del contrato publicada en BOCM el',None),
            
    
        )

        # response.xpath('//table/tbody/tr/td[contains (@class, "tdadjud")]/text()').get() adjudicatari

        # Look for contractors

        contractor_line = response.xpath('//table/tbody/tr')

        if contractor_line:
            for contractor in contractor_line:
                        
                contract_item['N_Lote'] = contractor.xpath('.//td[1]/text()').extract()
                contract_item['N_Ofertas'] = contractor.xpath('.//td[2]/text()').get()
                contract_item['Resultado'] = contractor.xpath('.//td[3]/text()').get()
                contract_item['NIF_adjudicatario'] = contractor.xpath('.//td[4]/text()').get()
                contract_item['Nombre_o_razón_social_adjudicatario'] = contractor.xpath('.//td[5]/text()').get()
                contract_item['Importe_adjudicación_sin_IVA'] = contractor.xpath('.//td[6]/text()').get()
                contract_item['Importe_adjudicación_con_IVA'] = contractor.xpath('.//td[7]/text()').get()
                yield contract_item
        else:
            yield contract_item




       