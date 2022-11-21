


# CMADRID CONTRACTS

WebScrapping project for "Tipologia i cicle de vida de les dades" at UOC (https://uoc.edu) by Miquel Piulats and Miquel Muntaner. 

It scraps the "Buscador avanzado de contratos" of the "Portal de la Contratación Pública de la Comunidad de Madrid" and creates a dataset with all "Negociado sin publicidad" contracts.

## Usage

scrapy crawl cmadrid -O data/data.csv

## Options

It can also scrap other type of contracts using the folowing url as starting url:

Abierto [http://www.madrid.org/cs/Satellite?c=Page&cid=1224915242285&codigo=PCON_&idPagina=1224915242285&language=es&newPagina=1&numPagListado=5&pagename=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&paginaActual=2&paginasTotal=3635&procedimientoAdjudicacion=Abierto&rootelement=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&site=PortalContratacion]


Negociado con publicidad [http://www.madrid.org/cs/Satellite?c=Page&cid=1224915242285&codigo=PCON_&idPagina=1224915242285&language=es&newPagina=1&numPagListado=5&pagename=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&paginaActual=2&paginasTotal=17&procedimientoAdjudicacion=Negociado+con+publicidad&rootelement=PortalContratacion%2FComunes%2FPresentacion%2FPCON_resultadoBuscadorAvanzado&site=PortalContratacion]

## Dataset

Last dataset can be found under data directory.

## License

Reconeixement-NoComercial 4.0 Internacional de Creative Commons [(https://i.creativecommons.org/l/by-nc/4.0/80x15.png)](http://creativecommons.org/licenses/by-nc/4.0/)


