# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ContractItem(scrapy.Item):
    # define the fields for your item here like:
    
    url = scrapy.Field()
    plazo = scrapy.Field()
    Objeto_del_contrato = scrapy.Field()
    Estado_de_la_licitación = scrapy.Field()
    Tipo_resolución = scrapy.Field()
    Tipo_Publicación = scrapy.Field()
    Código_CPV = scrapy.Field()
    Compra_pública_innovadora = scrapy.Field()
    Número_de_expediente = scrapy.Field()
    Referencia = scrapy.Field()
    Tipo_de_contrato = scrapy.Field()
    Entidad_adjudicadora = scrapy.Field()
    Procedimiento_Adjudicación = scrapy.Field()
    Valor_estimado_sin_IVA = scrapy.Field()
    Presupuesto_base_licitación_sin_impuestos = scrapy.Field()
    Presupuesto_base_licitación_Importe_total = scrapy.Field()
    Duración_del_contrato = scrapy.Field()
    Puntos_de_Información = scrapy.Field()
    Adjudicación_del_contrato_publicada_el = scrapy.Field()
    Formalización_del_contrato_publicada_el = scrapy.Field()
    Formalización_del_contrato_publicada_en_BOCM_el = scrapy.Field()
    NIF_adjudicatario = scrapy.Field()
    Nombre_o_razón_social_adjudicatario = scrapy.Field()
    Importe_adjudicación_sin_IVA = scrapy.Field()
    Importe_adjudicación_con_IVA = scrapy.Field()
    N_Lote = scrapy.Field()
    N_Ofertas = scrapy.Field()
    Resultado = scrapy.Field()


