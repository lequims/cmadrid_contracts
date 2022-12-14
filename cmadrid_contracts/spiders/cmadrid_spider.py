import scrapy
from cmadrid_contracts.items import ContractItem


class Cmadrid_Spider(scrapy.Spider):
    
    # name of variable should be 'name' only
    name = "cmadrid" 
    
    # urls from which will be used to extract information
    # list should be named 'start_urls' only
    
    start_urls = ["http://www.madrid.org/cs/Satellite?c=Page&cid=1224915242285&codigo=PCON_&idPagina=1224915242285&language=es&newPagina=1&numPagListado=5&pagename=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&paginaActual=2&paginasTotal=1204&rootelement=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&site=PortalContratacion&tipoPublicacion=Contratos+adjudicados+por+procedimientos+sin+publicidad"]
    base_url = 'https://www.madrid.org/'

    def parse(self, response):

        all_contracts_in_page =  response.xpath('//div[contains(@class, "cajaBlanca")]/div[contains(@class, "cajaBlancaDosL")]')
        
        # Extrating link to every contract
        
        page = response.xpath('//div[contains(@class, "caja")]/ul/li/a[contains (@class, "activo")]/text()').get()
       
        for contract in all_contracts_in_page:
            
            contract_url = contract.xpath('.//a/@href').get()
            yield scrapy.Request(self.base_url + contract_url, callback=self.parse_contract, meta={'page': page})

        # Check is there are a next page link
        next_page = response.xpath('//div[contains(@id, "pagSup")]/div[contains(@class, "caja")]/ul/li/a[contains (@class, "activo")]/following::li/a/@href').get()

        # if a next page exists continue scraping
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
            field_name = field.xpath('.//strong/text()').get()
            value = field.xpath('.//strong/following::br/following::text()').get()
            
            if(field_name):
                data_fields[field_name] = value   

        contract_item = ContractItem(
            
            Objeto_del_contrato = response.xpath('//h2[contains(@class, "tit11gr3")]/text()').get(),
            plazo = response.xpath('//div[contains(@id, "cont_int_izdo")]/span/text()').get(),
            url = response.url,
            Estado_de_la_licitaci??n = data_fields.get('Estado de la licitaci??n',None),
            Tipo_resoluci??n = data_fields.get('Tipo resoluci??n',None),
            Tipo_Publicaci??n = data_fields.get('Tipo Publicaci??n',None),
            C??digo_CPV = data_fields.get('C??digo CPV',None),
            Compra_p??blica_innovadora = data_fields.get('Compra p??blica innovadora',None),
            N??mero_de_expediente = data_fields.get('N??mero de expediente',None),
            Referencia = data_fields.get('Referencia',None),
            Tipo_de_contrato = data_fields.get('Tipo de contrato',None),
            Entidad_adjudicadora = data_fields.get('Entidad adjudicadora',None),
            Procedimiento_Adjudicaci??n = data_fields.get('Procedimiento Adjudicaci??n',None),
            Valor_estimado_sin_IVA = data_fields.get('Valor estimado sin I.V.A',None),
            Presupuesto_base_licitaci??n_sin_impuestos = data_fields.get('Presupuesto base licitaci??n (sin impuestos)',None),
            Duraci??n_del_contrato = data_fields.get('Duraci??n del contrato',None),
            Presupuesto_base_licitaci??n_Importe_total = data_fields.get('Presupuesto base licitaci??n. Importe total',None),
            Puntos_de_Informaci??n = data_fields.get('Puntos de Informaci??n',None),
            Adjudicaci??n_del_contrato_publicada_el = data_fields.get('Adjudicaci??n del contrato publicada el',None),
            Formalizaci??n_del_contrato_publicada_el = data_fields.get('Formalizaci??n del contrato publicada el',None),
            Formalizaci??n_del_contrato_publicada_en_BOCM_el = data_fields.get('Formalizaci??n del contrato publicada en BOCM el',None),
            
    
        )

        # Look for contractors

        contractor_line = response.xpath('//table/tbody/tr')

        if contractor_line:
            for contractor in contractor_line:
                        
                contract_item['N_Lote'] = contractor.xpath('.//td[1]/text()').get()
                contract_item['N_Ofertas'] = contractor.xpath('.//td[2]/text()').get()
                contract_item['Resultado'] = contractor.xpath('.//td[3]/text()').get()
                contract_item['NIF_adjudicatario'] = contractor.xpath('.//td[4]/text()').get()
                contract_item['Nombre_o_raz??n_social_adjudicatario'] = contractor.xpath('.//td[5]/text()').get()
                contract_item['Importe_adjudicaci??n_sin_IVA'] = contractor.xpath('.//td[6]/text()').get()
                contract_item['Importe_adjudicaci??n_con_IVA'] = contractor.xpath('.//td[7]/text()').get()
                yield contract_item
        else:
            yield contract_item




       