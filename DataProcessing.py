# coding=utf-8
import CleanData, nltk, ClasificateProduct, unidecode, AttributeExtractor
from nltk.stem import SnowballStemmer
from re import search, IGNORECASE, sub
from nltk import word_tokenize
from sys import argv
from simplejson import loads, dumps


class AttributeValue(object):
    def __init__(self, attribute_id, attribute_value):
        self.attributes_id = attribute_id
        self.description = attribute_value if attribute_value else ''


def download_modules():
    nltk.download()


def process_data(json_data):
    stemmer = SnowballStemmer('spanish')
    attributes = ClasificateProduct.get_attributes(json_data)
    clean_data_line = CleanData.cleanData(json_data['description'])
    attribute_collected = list()
    for attribute in attributes:
        attribute_value = None
        # Limpia elementos innecesarios del atributo
        clean_attribute = sub('\(.*\)', '', attribute['value'])
        posible_attribute = get_attributes(clean_attribute, clean_data_line, stemmer)
        if not posible_attribute:
            for synonym_attr in get_synonyms(clean_attribute):
                posible_attribute = get_attributes(synonym_attr, clean_data_line, stemmer)
                if posible_attribute:
                    break
        if posible_attribute:
            attribute_value = AttributeExtractor.extract_atribute(posible_attribute, attribute)
        attribute_collected.append(dumps(AttributeValue(attribute['id'], attribute_value).__dict__))

    print dumps(attribute_collected)
    # print clean_data_line


def get_attributes(attribute, data_lines, stemmer):
    # print "Atributo "+attribute

    token_attribute_regex = ''
    for token_attribute in word_tokenize(attribute):
        token_attribute_regex = '{}{}{}'.format(token_attribute_regex, '.*', stemmer.stem(token_attribute))

    for line in data_lines:
        if search(token_attribute_regex, line, IGNORECASE):
            # print data_line_token
            return line


def get_synonyms(attribute):
    synonyms = list()
    # sinonimos para medidas de tamano
    synonyms_size = ['dimension', 'tamano']
    for synonym_size in synonyms_size:
        if search('largo|ancho|alto', attribute, IGNORECASE):
            synonyms.append(sub('(?i)(largo|ancho|alto)', synonym_size, attribute))
    return synonyms


def main():
    print '--------------------------------------'
    #data = unidecode.unidecode(argv[1].decode("utf-8"))
    data = unidecode.unidecode(
        r'{"description":"Color: Amatista, amarillo claro Y AMARILLO\n>>>>>Cargador Bateria Portátil Usb 10400 mAh<<<<<\n*La batería externa de 10.400 mAh Power Bank puede ser usada para cargar teléfonos celulares, tablets, o reproductores multimedia.\n*Es cómodo, con diseño moderno y fácil de usar.\n*Conveniente para recargar su teléfono u otros dispositivos móviles, en cualquier momento y cualquier lugar.\n*Cuenta con botos de encendido y luces Led indicador de carga\n*Capacidad: 3.6V/10.400 mAh\nEntrada: Micro USB 5V/2A\nSalida: USB: 5V/2.1A\nIncluye cable Usb\n*Dimensiones: 9.2 cm x 7.7 cm x 2.2 cm\nPeso: 198 gr\n*Empaque: 19 cm x 9.2 cm x 3 cm\nPeso: 232 gr","category":{"id":"J04030101","description":"","attributes_categories":[{"id":1189,"value":"Alto (cm)","observation":"dimension","types":[]},{"id":1190,"value":"Ancho (cm)","observation":"dimension","types":[]},{"id":1191,"value":"Largo (cm)","observation":"capacidad","types":[]},{"id":1192,"value":"Peso (gr)","observation":"masa","types":[]},{"id":1193,"value":"Tipo","observation":"opciones","types":[{"id":72893,"type":"Vestidos","attributes_id":1193},{"id":72894,"type":"Enteritos","attributes_id":1193},{"id":72895,"type":"Salidas de baño","attributes_id":1193}]},{"id":1194,"value":"Género","observation":"","types":[{"id":72896,"type":"Mujer","attributes_id":1194},{"id":72897,"type":"Unisex","attributes_id":1194}]},{"id":1195,"value":"Estilo","observation":"","types":[{"id":72898,"type":"Casual","attributes_id":1195},{"id":72899,"type":"Vestir","attributes_id":1195},{"id":72900,"type":"Fiesta","attributes_id":1195},{"id":72901,"type":"Deportivo","attributes_id":1195},{"id":72902,"type":"Playa","attributes_id":1195}]},{"id":1196,"value":"Temporada","observation":"","types":[{"id":72903,"type":"Otoño-Invierno","attributes_id":1196},{"id":72904,"type":"Primavera-Verano","attributes_id":1196},{"id":72905,"type":"Toda temporada","attributes_id":1196}]},{"id":1197,"value":"Talla","observation":"","types":[{"id":72906,"type":"0","attributes_id":1197},{"id":72907,"type":"1","attributes_id":1197},{"id":72908,"type":"3","attributes_id":1197},{"id":72909,"type":"3.5","attributes_id":1197},{"id":72910,"type":"4","attributes_id":1197},{"id":72911,"type":"4.5","attributes_id":1197},{"id":72912,"type":"5","attributes_id":1197},{"id":72913,"type":"5.5","attributes_id":1197},{"id":72914,"type":"6","attributes_id":1197},{"id":72915,"type":"6.5","attributes_id":1197},{"id":72916,"type":"7","attributes_id":1197},{"id":72917,"type":"7.5","attributes_id":1197},{"id":72918,"type":"8","attributes_id":1197},{"id":72919,"type":"8.5","attributes_id":1197},{"id":72920,"type":"9","attributes_id":1197},{"id":72921,"type":"9.5","attributes_id":1197},{"id":72922,"type":"10","attributes_id":1197},{"id":72923,"type":"10.5","attributes_id":1197},{"id":72924,"type":"11","attributes_id":1197},{"id":72925,"type":"11.5","attributes_id":1197},{"id":72926,"type":"12","attributes_id":1197},{"id":72927,"type":"13","attributes_id":1197},{"id":72928,"type":"14","attributes_id":1197},{"id":72929,"type":"15","attributes_id":1197},{"id":72930,"type":"16","attributes_id":1197},{"id":72931,"type":"17","attributes_id":1197},{"id":72932,"type":"18","attributes_id":1197},{"id":72933,"type":"19","attributes_id":1197},{"id":72934,"type":"20","attributes_id":1197},{"id":72935,"type":"21","attributes_id":1197},{"id":72936,"type":"22","attributes_id":1197},{"id":72937,"type":"23","attributes_id":1197},{"id":72938,"type":"24","attributes_id":1197},{"id":72939,"type":"25","attributes_id":1197},{"id":72940,"type":"26","attributes_id":1197},{"id":72941,"type":"27","attributes_id":1197},{"id":72942,"type":"28","attributes_id":1197},{"id":72943,"type":"29","attributes_id":1197},{"id":72944,"type":"30","attributes_id":1197},{"id":72945,"type":"31","attributes_id":1197},{"id":72946,"type":"32","attributes_id":1197},{"id":72947,"type":"33","attributes_id":1197},{"id":72948,"type":"34","attributes_id":1197},{"id":72949,"type":"35","attributes_id":1197},{"id":72950,"type":"36","attributes_id":1197},{"id":72951,"type":"37","attributes_id":1197},{"id":72952,"type":"38","attributes_id":1197},{"id":72953,"type":"39","attributes_id":1197},{"id":72954,"type":"40","attributes_id":1197},{"id":72955,"type":"41","attributes_id":1197},{"id":72956,"type":"42","attributes_id":1197},{"id":72957,"type":"43","attributes_id":1197},{"id":72958,"type":"44","attributes_id":1197},{"id":72959,"type":"45","attributes_id":1197},{"id":72960,"type":"46","attributes_id":1197},{"id":72961,"type":"47","attributes_id":1197},{"id":72962,"type":"48","attributes_id":1197},{"id":72963,"type":"49","attributes_id":1197},{"id":72964,"type":"50","attributes_id":1197},{"id":72965,"type":"51","attributes_id":1197},{"id":72966,"type":"52","attributes_id":1197},{"id":72967,"type":"53","attributes_id":1197},{"id":72968,"type":"54","attributes_id":1197},{"id":72969,"type":"55","attributes_id":1197},{"id":72970,"type":"56","attributes_id":1197},{"id":72971,"type":"57","attributes_id":1197},{"id":72972,"type":"58","attributes_id":1197},{"id":72973,"type":"59","attributes_id":1197},{"id":72974,"type":"60","attributes_id":1197},{"id":72975,"type":"65","attributes_id":1197},{"id":72976,"type":"70","attributes_id":1197},{"id":72977,"type":"75","attributes_id":1197},{"id":72978,"type":"80","attributes_id":1197},{"id":72979,"type":"85","attributes_id":1197},{"id":72980,"type":"90","attributes_id":1197},{"id":72981,"type":"95","attributes_id":1197},{"id":72982,"type":"96","attributes_id":1197},{"id":72983,"type":"97","attributes_id":1197},{"id":72984,"type":"98","attributes_id":1197},{"id":72985,"type":"99","attributes_id":1197},{"id":72986,"type":"100","attributes_id":1197},{"id":72987,"type":"101","attributes_id":1197},{"id":72988,"type":"102","attributes_id":1197},{"id":72989,"type":"103","attributes_id":1197},{"id":72990,"type":"104","attributes_id":1197},{"id":72991,"type":"105","attributes_id":1197},{"id":72992,"type":"106","attributes_id":1197},{"id":72993,"type":"107","attributes_id":1197},{"id":72994,"type":"108","attributes_id":1197},{"id":72995,"type":"109","attributes_id":1197},{"id":72996,"type":"110","attributes_id":1197},{"id":72997,"type":"111","attributes_id":1197},{"id":72998,"type":"112","attributes_id":1197},{"id":72999,"type":"113","attributes_id":1197},{"id":73000,"type":"114","attributes_id":1197},{"id":73001,"type":"115","attributes_id":1197},{"id":73002,"type":"116","attributes_id":1197},{"id":73003,"type":"117","attributes_id":1197},{"id":73004,"type":"118","attributes_id":1197},{"id":73005,"type":"119","attributes_id":1197},{"id":73006,"type":"120","attributes_id":1197},{"id":73007,"type":"1,5P","attributes_id":1197},{"id":73008,"type":"10/11","attributes_id":1197},{"id":73009,"type":"10/13","attributes_id":1197},{"id":73010,"type":"100B","attributes_id":1197},{"id":73011,"type":"100C","attributes_id":1197},{"id":73012,"type":"100D","attributes_id":1197},{"id":73013,"type":"100DD","attributes_id":1197},{"id":73014,"type":"105B","attributes_id":1197},{"id":73015,"type":"105C","attributes_id":1197},{"id":73016,"type":"105D","attributes_id":1197},{"id":73017,"type":"105DD","attributes_id":1197},{"id":73018,"type":"12M","attributes_id":1197},{"id":73019,"type":"15,5A","attributes_id":1197},{"id":73020,"type":"15,5B","attributes_id":1197},{"id":73021,"type":"15,5C","attributes_id":1197},{"id":73022,"type":"15,5D","attributes_id":1197},{"id":73023,"type":"15,5E","attributes_id":1197},{"id":73024,"type":"15,5F","attributes_id":1197},{"id":73025,"type":"15A","attributes_id":1197},{"id":73026,"type":"15B","attributes_id":1197},{"id":73027,"type":"15C","attributes_id":1197},{"id":73028,"type":"15D","attributes_id":1197},{"id":73029,"type":"15,0","attributes_id":1197},{"id":73030,"type":"15,5","attributes_id":1197},{"id":73031,"type":"16,0","attributes_id":1197},{"id":73032,"type":"16,5","attributes_id":1197},{"id":73033,"type":"12,5","attributes_id":1197},{"id":73034,"type":"16,5D","attributes_id":1197},{"id":73035,"type":"16,5E","attributes_id":1197},{"id":73036,"type":"16,5F","attributes_id":1197},{"id":73037,"type":"16A","attributes_id":1197},{"id":73038,"type":"16B","attributes_id":1197},{"id":73039,"type":"16C","attributes_id":1197},{"id":73040,"type":"16D","attributes_id":1197},{"id":73041,"type":"16E","attributes_id":1197},{"id":73042,"type":"16F","attributes_id":1197},{"id":73043,"type":"17,0","attributes_id":1197},{"id":73044,"type":"17,5","attributes_id":1197},{"id":73045,"type":"17,5C","attributes_id":1197},{"id":73046,"type":"17,5D","attributes_id":1197},{"id":73047,"type":"17,5E","attributes_id":1197},{"id":73048,"type":"17,5F","attributes_id":1197},{"id":73049,"type":"17A","attributes_id":1197},{"id":73050,"type":"17B","attributes_id":1197},{"id":73051,"type":"17C","attributes_id":1197},{"id":73052,"type":"17D","attributes_id":1197},{"id":73053,"type":"17E","attributes_id":1197},{"id":73054,"type":"17F","attributes_id":1197},{"id":73055,"type":"18,0","attributes_id":1197},{"id":73056,"type":"18,5","attributes_id":1197},{"id":73057,"type":"18C","attributes_id":1197},{"id":73058,"type":"18D","attributes_id":1197},{"id":73059,"type":"18E","attributes_id":1197},{"id":73060,"type":"18F","attributes_id":1197},{"id":73061,"type":"18M","attributes_id":1197},{"id":73062,"type":"1M","attributes_id":1197},{"id":73063,"type":"1P","attributes_id":1197},{"id":73064,"type":"24M","attributes_id":1197},{"id":73065,"type":"2P","attributes_id":1197},{"id":73066,"type":"30A","attributes_id":1197},{"id":73067,"type":"30AA","attributes_id":1197},{"id":73068,"type":"30B","attributes_id":1197},{"id":73069,"type":"30C","attributes_id":1197},{"id":73070,"type":"32A","attributes_id":1197},{"id":73071,"type":"32AA","attributes_id":1197},{"id":73072,"type":"32B","attributes_id":1197},{"id":73073,"type":"32C","attributes_id":1197},{"id":73074,"type":"34A","attributes_id":1197},{"id":73075,"type":"34AA","attributes_id":1197},{"id":73076,"type":"34B","attributes_id":1197},{"id":73077,"type":"34C","attributes_id":1197},{"id":73078,"type":"34D","attributes_id":1197},{"id":73079,"type":"34DD","attributes_id":1197},{"id":73080,"type":"36AA","attributes_id":1197},{"id":73081,"type":"36B","attributes_id":1197},{"id":73082,"type":"36C","attributes_id":1197},{"id":73083,"type":"36D","attributes_id":1197},{"id":73084,"type":"36DD","attributes_id":1197},{"id":73085,"type":"36M","attributes_id":1197},{"id":73086,"type":"38B","attributes_id":1197},{"id":73087,"type":"38C","attributes_id":1197},{"id":73088,"type":"38D","attributes_id":1197},{"id":73089,"type":"38DD","attributes_id":1197},{"id":73090,"type":"3M","attributes_id":1197},{"id":73091,"type":"40B","attributes_id":1197},{"id":73092,"type":"40C","attributes_id":1197},{"id":73093,"type":"40D","attributes_id":1197},{"id":73094,"type":"40DD","attributes_id":1197},{"id":73095,"type":"42B","attributes_id":1197},{"id":73096,"type":"42C","attributes_id":1197},{"id":73097,"type":"42D","attributes_id":1197},{"id":73098,"type":"42DD","attributes_id":1197},{"id":73099,"type":"44B","attributes_id":1197},{"id":73100,"type":"44C","attributes_id":1197},{"id":73101,"type":"44D","attributes_id":1197},{"id":73102,"type":"44DD","attributes_id":1197},{"id":73103,"type":"6M","attributes_id":1197},{"id":73104,"type":"7/8","attributes_id":1197},{"id":73105,"type":"70A","attributes_id":1197},{"id":73106,"type":"70AA","attributes_id":1197},{"id":73107,"type":"70B","attributes_id":1197},{"id":73108,"type":"70C","attributes_id":1197},{"id":73109,"type":"75A","attributes_id":1197},{"id":73110,"type":"75B","attributes_id":1197},{"id":73111,"type":"75C","attributes_id":1197},{"id":73112,"type":"80B","attributes_id":1197},{"id":73113,"type":"80C","attributes_id":1197},{"id":73114,"type":"80D","attributes_id":1197},{"id":73115,"type":"80DD","attributes_id":1197},{"id":73116,"type":"85B","attributes_id":1197},{"id":73117,"type":"85C","attributes_id":1197},{"id":73118,"type":"85D","attributes_id":1197},{"id":73119,"type":"85DD","attributes_id":1197},{"id":73120,"type":"9/10","attributes_id":1197},{"id":73121,"type":"9/11","attributes_id":1197},{"id":73122,"type":"90B","attributes_id":1197},{"id":73123,"type":"90C","attributes_id":1197},{"id":73124,"type":"90D","attributes_id":1197},{"id":73125,"type":"90DD","attributes_id":1197},{"id":73126,"type":"95B","attributes_id":1197},{"id":73127,"type":"95C","attributes_id":1197},{"id":73128,"type":"95D","attributes_id":1197},{"id":73129,"type":"95DD","attributes_id":1197},{"id":73130,"type":"9M","attributes_id":1197},{"id":73131,"type":"ALH1","attributes_id":1197},{"id":73132,"type":"ALH2","attributes_id":1197},{"id":73133,"type":"AP1","attributes_id":1197},{"id":73134,"type":"AP2","attributes_id":1197},{"id":73135,"type":"AP3","attributes_id":1197},{"id":73136,"type":"ARD1","attributes_id":1197},{"id":73137,"type":"ARD2","attributes_id":1197},{"id":73138,"type":"ART1","attributes_id":1197},{"id":73139,"type":"ART2","attributes_id":1197},{"id":73140,"type":"ART3","attributes_id":1197},{"id":73141,"type":"ART4","attributes_id":1197},{"id":73142,"type":"ART5","attributes_id":1197},{"id":73143,"type":"ART6","attributes_id":1197},{"id":73144,"type":"ART7","attributes_id":1197},{"id":73145,"type":"ART8","attributes_id":1197},{"id":73146,"type":"ART9","attributes_id":1197},{"id":73147,"type":"C4X4","attributes_id":1197},{"id":73148,"type":"C5X5","attributes_id":1197},{"id":73149,"type":"C6X6","attributes_id":1197},{"id":73150,"type":"CHA1","attributes_id":1197},{"id":73151,"type":"IND1","attributes_id":1197},{"id":73152,"type":"K","attributes_id":1197},{"id":73153,"type":"L","attributes_id":1197},{"id":73154,"type":"M","attributes_id":1197},{"id":73155,"type":"OV10P","attributes_id":1197},{"id":73156,"type":"OV8P","attributes_id":1197},{"id":73157,"type":"RD6P","attributes_id":1197},{"id":73158,"type":"RT10P","attributes_id":1197},{"id":73159,"type":"RT12P","attributes_id":1197},{"id":73160,"type":"RT8P","attributes_id":1197},{"id":73161,"type":"S","attributes_id":1197},{"id":73162,"type":"SK","attributes_id":1197},{"id":73163,"type":"TN1","attributes_id":1197},{"id":73164,"type":"TN2","attributes_id":1197},{"id":73165,"type":"TN3","attributes_id":1197},{"id":73166,"type":"TN4","attributes_id":1197},{"id":73167,"type":"TN5","attributes_id":1197},{"id":73168,"type":"TN6","attributes_id":1197},{"id":73169,"type":"TN7","attributes_id":1197},{"id":73170,"type":"TP1","attributes_id":1197},{"id":73171,"type":"TP2","attributes_id":1197},{"id":73172,"type":"TP3","attributes_id":1197},{"id":73173,"type":"TP4","attributes_id":1197},{"id":73174,"type":"TU","attributes_id":1197},{"id":73175,"type":"XL","attributes_id":1197},{"id":73176,"type":"XS","attributes_id":1197},{"id":73177,"type":"XXL","attributes_id":1197},{"id":73178,"type":"XXS","attributes_id":1197},{"id":73179,"type":"35.5","attributes_id":1197},{"id":73180,"type":"36.5","attributes_id":1197},{"id":73181,"type":"37.5","attributes_id":1197},{"id":73182,"type":"38.5","attributes_id":1197},{"id":73183,"type":"N/A","attributes_id":1197},{"id":73184,"type":"31-31","attributes_id":1197},{"id":73185,"type":"32-32","attributes_id":1197},{"id":73186,"type":"33-31","attributes_id":1197},{"id":73187,"type":"33-32","attributes_id":1197},{"id":73188,"type":"34-31","attributes_id":1197},{"id":73189,"type":"34-32","attributes_id":1197},{"id":73190,"type":"34-33","attributes_id":1197},{"id":73191,"type":"34-34","attributes_id":1197},{"id":73192,"type":"35-31","attributes_id":1197},{"id":73193,"type":"35-32","attributes_id":1197},{"id":73194,"type":"35-33","attributes_id":1197},{"id":73195,"type":"35-34","attributes_id":1197},{"id":73196,"type":"36-31","attributes_id":1197},{"id":73197,"type":"36-32","attributes_id":1197},{"id":73198,"type":"36-33","attributes_id":1197},{"id":73199,"type":"37-31","attributes_id":1197},{"id":73200,"type":"37-32","attributes_id":1197},{"id":73201,"type":"38-32","attributes_id":1197},{"id":73202,"type":"40-32","attributes_id":1197},{"id":73203,"type":"70D","attributes_id":1197},{"id":73204,"type":"75D","attributes_id":1197},{"id":73205,"type":"75DD","attributes_id":1197},{"id":73206,"type":"75E","attributes_id":1197},{"id":73207,"type":"80E","attributes_id":1197},{"id":73208,"type":"90E","attributes_id":1197},{"id":73209,"type":"85E","attributes_id":1197},{"id":73210,"type":"2","attributes_id":1197},{"id":73211,"type":"12.5","attributes_id":1197},{"id":73212,"type":"13.5","attributes_id":1197},{"id":73213,"type":"14.5","attributes_id":1197},{"id":73214,"type":"15N","attributes_id":1197},{"id":73215,"type":"15.5N","attributes_id":1197},{"id":73216,"type":"16N","attributes_id":1197},{"id":73217,"type":"16.5N","attributes_id":1197},{"id":73218,"type":"17N","attributes_id":1197},{"id":73219,"type":"17.5N","attributes_id":1197},{"id":73220,"type":"18N","attributes_id":1197},{"id":73221,"type":"33/34","attributes_id":1197},{"id":73222,"type":"34/35","attributes_id":1197},{"id":73223,"type":"1.5","attributes_id":1197},{"id":73224,"type":"2.5","attributes_id":1197},{"id":73225,"type":"0M","attributes_id":1197},{"id":73226,"type":"3A","attributes_id":1197},{"id":73227,"type":"4A","attributes_id":1197},{"id":73228,"type":"6A","attributes_id":1197},{"id":73229,"type":"8A","attributes_id":1197},{"id":73230,"type":"10A","attributes_id":1197},{"id":73231,"type":"00M","attributes_id":1197},{"id":73232,"type":"L 33","attributes_id":1197},{"id":73233,"type":"L 35","attributes_id":1197},{"id":73234,"type":"80A","attributes_id":1197},{"id":73235,"type":"85A","attributes_id":1197},{"id":73236,"type":"151","attributes_id":1197},{"id":73237,"type":"161","attributes_id":1197},{"id":73238,"type":"156","attributes_id":1197},{"id":73239,"type":"146","attributes_id":1197},{"id":73240,"type":"166","attributes_id":1197},{"id":73241,"type":"140","attributes_id":1197},{"id":73242,"type":"145","attributes_id":1197},{"id":73243,"type":"150","attributes_id":1197},{"id":73244,"type":"155","attributes_id":1197},{"id":73245,"type":"160","attributes_id":1197},{"id":73246,"type":"165","attributes_id":1197},{"id":73247,"type":"62","attributes_id":1197},{"id":73248,"type":"125","attributes_id":1197},{"id":73249,"type":"130","attributes_id":1197},{"id":73250,"type":"135","attributes_id":1197},{"id":73251,"type":"25,5","attributes_id":1197},{"id":73252,"type":"26,5","attributes_id":1197},{"id":73253,"type":"27,5","attributes_id":1197},{"id":73254,"type":"28,5","attributes_id":1197},{"id":73255,"type":"29,5","attributes_id":1197},{"id":73256,"type":"23,5","attributes_id":1197},{"id":73257,"type":"24,5","attributes_id":1197},{"id":73258,"type":"25,0","attributes_id":1197},{"id":73259,"type":"30,5","attributes_id":1197},{"id":73260,"type":"170","attributes_id":1197},{"id":73261,"type":"180","attributes_id":1197},{"id":73262,"type":"140,0","attributes_id":1197},{"id":73263,"type":"OG","attributes_id":1197},{"id":73264,"type":"OSFA","attributes_id":1197},{"id":73265,"type":"64","attributes_id":1197},{"id":73266,"type":"0/0","attributes_id":1197},{"id":73267,"type":"1/2","attributes_id":1197},{"id":73268,"type":"2/4","attributes_id":1197},{"id":73269,"type":"3/5","attributes_id":1197},{"id":73270,"type":"6/8","attributes_id":1197},{"id":73271,"type":"3/4","attributes_id":1197},{"id":73272,"type":"5/6","attributes_id":1197},{"id":73273,"type":"0/12","attributes_id":1197},{"id":73274,"type":"0/1","attributes_id":1197},{"id":73275,"type":"2/3","attributes_id":1197},{"id":73276,"type":"4/5","attributes_id":1197},{"id":73277,"type":"6/7","attributes_id":1197},{"id":73278,"type":"8/9","attributes_id":1197},{"id":73279,"type":"A","attributes_id":1197},{"id":73280,"type":"B","attributes_id":1197},{"id":73281,"type":"36A","attributes_id":1197},{"id":73282,"type":"36-34","attributes_id":1197},{"id":73283,"type":"38-34","attributes_id":1197},{"id":73284,"type":"40-34","attributes_id":1197},{"id":73285,"type":"9/12","attributes_id":1197},{"id":73286,"type":"JR","attributes_id":1197},{"id":73287,"type":"0/2","attributes_id":1197},{"id":73288,"type":"10/12","attributes_id":1197},{"id":73289,"type":"15E","attributes_id":1197},{"id":73290,"type":"14/16","attributes_id":1197},{"id":73291,"type":"2T","attributes_id":1197},{"id":73292,"type":"3T","attributes_id":1197},{"id":73293,"type":"4/5_2","attributes_id":1197},{"id":73294,"type":"4T","attributes_id":1197},{"id":73295,"type":"6/6X","attributes_id":1197},{"id":73296,"type":"6/7_2","attributes_id":1197},{"id":73297,"type":"7/8_2","attributes_id":1197},{"id":73298,"type":"38A","attributes_id":1197},{"id":73299,"type":"39,5","attributes_id":1197},{"id":73300,"type":"40,5","attributes_id":1197},{"id":73301,"type":"41,5","attributes_id":1197},{"id":73302,"type":"42,5","attributes_id":1197},{"id":73303,"type":"43,5","attributes_id":1197},{"id":73304,"type":"6L","attributes_id":1197},{"id":73305,"type":"S/M","attributes_id":1197},{"id":73306,"type":"L/XL","attributes_id":1197},{"id":73307,"type":"44,5","attributes_id":1197},{"id":73308,"type":"30-34","attributes_id":1197},{"id":73309,"type":"32/30","attributes_id":1197},{"id":73310,"type":"33-34","attributes_id":1197},{"id":73311,"type":"34/30","attributes_id":1197},{"id":73312,"type":"35/30","attributes_id":1197},{"id":73313,"type":"36-34","attributes_id":1197},{"id":73314,"type":"38/30","attributes_id":1197},{"id":73315,"type":"40/30","attributes_id":1197},{"id":73316,"type":"32/33","attributes_id":1197},{"id":73317,"type":"33/33","attributes_id":1197},{"id":73318,"type":"34/33","attributes_id":1197},{"id":73319,"type":"35/33","attributes_id":1197},{"id":73320,"type":"36/33","attributes_id":1197},{"id":73321,"type":"38/33","attributes_id":1197},{"id":73322,"type":"40/33","attributes_id":1197},{"id":73323,"type":"15.5","attributes_id":1197},{"id":73324,"type":"16.5","attributes_id":1197},{"id":73325,"type":"17.5","attributes_id":1197},{"id":73326,"type":"15-33","attributes_id":1197},{"id":73327,"type":"152-32","attributes_id":1197},{"id":73328,"type":"152-33","attributes_id":1197},{"id":73329,"type":"152-34","attributes_id":1197},{"id":73330,"type":"16-34","attributes_id":1197},{"id":73331,"type":"16-35","attributes_id":1197},{"id":73332,"type":"165-33","attributes_id":1197},{"id":73333,"type":"165-34","attributes_id":1197},{"id":73334,"type":"165-35","attributes_id":1197},{"id":73335,"type":"17-33","attributes_id":1197},{"id":73336,"type":"17-34","attributes_id":1197},{"id":73337,"type":"17-35","attributes_id":1197},{"id":73338,"type":"175-34","attributes_id":1197},{"id":73339,"type":"175-35","attributes_id":1197},{"id":73340,"type":"30-32","attributes_id":1197},{"id":73341,"type":"32-30","attributes_id":1197},{"id":73342,"type":"33-30","attributes_id":1197},{"id":73343,"type":"34-30","attributes_id":1197},{"id":73344,"type":"36-30","attributes_id":1197},{"id":73345,"type":"38-30","attributes_id":1197},{"id":73346,"type":"42-32","attributes_id":1197},{"id":73347,"type":"32-34","attributes_id":1197},{"id":73348,"type":"30-30","attributes_id":1197},{"id":73349,"type":"40-30","attributes_id":1197},{"id":73350,"type":"42-30","attributes_id":1197},{"id":73351,"type":"15-3","attributes_id":1197},{"id":73352,"type":"15-34","attributes_id":1197},{"id":73353,"type":"35-30","attributes_id":1197},{"id":73354,"type":"15-23","attributes_id":1197},{"id":73355,"type":"15/-23","attributes_id":1197},{"id":73356,"type":"16-23","attributes_id":1197},{"id":73357,"type":"16/-23","attributes_id":1197},{"id":73358,"type":"16-45","attributes_id":1197},{"id":73359,"type":"16/-45","attributes_id":1197},{"id":73360,"type":"17-45","attributes_id":1197},{"id":73361,"type":"17/-45","attributes_id":1197},{"id":73362,"type":"16-33","attributes_id":1197},{"id":73363,"type":"16-36","attributes_id":1197},{"id":73364,"type":"15-35","attributes_id":1197},{"id":73365,"type":"18-45","attributes_id":1197},{"id":73366,"type":"16-32","attributes_id":1197},{"id":73367,"type":"17-36","attributes_id":1197},{"id":73368,"type":"14-32","attributes_id":1197},{"id":73369,"type":"14-33","attributes_id":1197},{"id":73370,"type":"44-32","attributes_id":1197},{"id":73371,"type":"38R","attributes_id":1197},{"id":73372,"type":"40R","attributes_id":1197},{"id":73373,"type":"40L","attributes_id":1197},{"id":73374,"type":"41L","attributes_id":1197},{"id":73375,"type":"42SH","attributes_id":1197},{"id":73376,"type":"42R","attributes_id":1197},{"id":73377,"type":"42L","attributes_id":1197},{"id":73378,"type":"43R","attributes_id":1197},{"id":73379,"type":"43L","attributes_id":1197},{"id":73380,"type":"44R","attributes_id":1197},{"id":73381,"type":"44L","attributes_id":1197},{"id":73382,"type":"46R","attributes_id":1197},{"id":73383,"type":"46L","attributes_id":1197},{"id":73384,"type":"48R","attributes_id":1197},{"id":73385,"type":"48L","attributes_id":1197},{"id":73386,"type":"14-34","attributes_id":1197},{"id":73387,"type":"18-34","attributes_id":1197},{"id":73388,"type":"18-35","attributes_id":1197},{"id":73389,"type":"18-36","attributes_id":1197},{"id":73390,"type":"18-33","attributes_id":1197},{"id":73391,"type":"15/32","attributes_id":1197},{"id":73392,"type":"15/33","attributes_id":1197},{"id":73393,"type":"15/34","attributes_id":1197},{"id":73394,"type":"16/33","attributes_id":1197},{"id":73395,"type":"16/34","attributes_id":1197},{"id":73396,"type":"16/36","attributes_id":1197},{"id":73397,"type":"16/35","attributes_id":1197},{"id":73398,"type":"17/33","attributes_id":1197},{"id":73399,"type":"17/34","attributes_id":1197},{"id":73400,"type":"17/35","attributes_id":1197},{"id":73401,"type":"15/35","attributes_id":1197},{"id":73402,"type":"17/36","attributes_id":1197},{"id":73403,"type":"14/32","attributes_id":1197},{"id":73404,"type":"14/33","attributes_id":1197},{"id":73405,"type":"14/34","attributes_id":1197},{"id":73406,"type":"15-32","attributes_id":1197},{"id":73407,"type":"30/33","attributes_id":1197},{"id":73408,"type":"15/23","attributes_id":1197},{"id":73409,"type":"15/45","attributes_id":1197},{"id":73410,"type":"16/23","attributes_id":1197},{"id":73411,"type":"16/45","attributes_id":1197},{"id":73412,"type":"17/45","attributes_id":1197},{"id":73413,"type":"17-23","attributes_id":1197},{"id":73414,"type":"17/23","attributes_id":1197},{"id":73415,"type":"5/8","attributes_id":1197},{"id":73416,"type":"L/X","attributes_id":1197},{"id":73417,"type":"18.5","attributes_id":1197},{"id":73418,"type":"30/30","attributes_id":1197},{"id":73419,"type":"33/30","attributes_id":1197},{"id":73420,"type":"36/30","attributes_id":1197},{"id":73421,"type":"38SH","attributes_id":1197},{"id":73422,"type":"40SH","attributes_id":1197},{"id":73423,"type":"41R","attributes_id":1197},{"id":73424,"type":"15-32","attributes_id":1197},{"id":73425,"type":"15-33","attributes_id":1197},{"id":73426,"type":"15-34","attributes_id":1197},{"id":73427,"type":"16-32","attributes_id":1197},{"id":73428,"type":"16-33","attributes_id":1197},{"id":73429,"type":"16-34","attributes_id":1197},{"id":73430,"type":"16-35","attributes_id":1197},{"id":73431,"type":"16-36","attributes_id":1197},{"id":73432,"type":"17-33","attributes_id":1197},{"id":73433,"type":"17-34","attributes_id":1197},{"id":73434,"type":"17-35","attributes_id":1197},{"id":73435,"type":"17-36","attributes_id":1197},{"id":73436,"type":"14.5","attributes_id":1197},{"id":73437,"type":"66","attributes_id":1197},{"id":73438,"type":"67","attributes_id":1197},{"id":73439,"type":"69","attributes_id":1197},{"id":73440,"type":"91","attributes_id":1197},{"id":73441,"type":"63","attributes_id":1197},{"id":73442,"type":"0-2","attributes_id":1197},{"id":73443,"type":"0-4","attributes_id":1197},{"id":73444,"type":"0-6","attributes_id":1197},{"id":73445,"type":"10-13","attributes_id":1197},{"id":73446,"type":"10MZ","attributes_id":1197},{"id":73447,"type":"11-12","attributes_id":1197},{"id":73448,"type":"11MZ","attributes_id":1197},{"id":73449,"type":"12-18","attributes_id":1197},{"id":73450,"type":"19-21","attributes_id":1197},{"id":73451,"type":"22-24","attributes_id":1197},{"id":73452,"type":"2-4","attributes_id":1197},{"id":73453,"type":"25-27","attributes_id":1197},{"id":73454,"type":"28-30","attributes_id":1197},{"id":73455,"type":"31-33","attributes_id":1197},{"id":73456,"type":"3-4","attributes_id":1197},{"id":73457,"type":"34-36","attributes_id":1197},{"id":73458,"type":"35-37","attributes_id":1197},{"id":73459,"type":"37-39","attributes_id":1197},{"id":73460,"type":"38-40","attributes_id":1197},{"id":73461,"type":"40-41","attributes_id":1197},{"id":73462,"type":"41-43","attributes_id":1197},{"id":73463,"type":"42-43","attributes_id":1197},{"id":73464,"type":"44-45","attributes_id":1197},{"id":73465,"type":"44-46","attributes_id":1197},{"id":73466,"type":"4-6","attributes_id":1197},{"id":73467,"type":"46-47","attributes_id":1197},{"id":73468,"type":"4-8","attributes_id":1197},{"id":73469,"type":"4C","attributes_id":1197},{"id":73470,"type":"5-6","attributes_id":1197},{"id":73471,"type":"5-8","attributes_id":1197},{"id":73472,"type":"5C","attributes_id":1197},{"id":73473,"type":"6-12","attributes_id":1197},{"id":73474,"type":"6-8","attributes_id":1197},{"id":73475,"type":"7-8","attributes_id":1197},{"id":73476,"type":"8-10","attributes_id":1197},{"id":73477,"type":"8-12","attributes_id":1197},{"id":73478,"type":"9-10","attributes_id":1197},{"id":73479,"type":"9-13","attributes_id":1197},{"id":73480,"type":"XLLON","attributes_id":1197},{"id":73481,"type":"XLSHO","attributes_id":1197},{"id":73482,"type":"12MZ","attributes_id":1197},{"id":73483,"type":"15-18","attributes_id":1197},{"id":73484,"type":"3C","attributes_id":1197},{"id":73485,"type":"XXXL","attributes_id":1197},{"id":73486,"type":"M/L","attributes_id":1197},{"id":73487,"type":"68","attributes_id":1197},{"id":73488,"type":"37-41","attributes_id":1197},{"id":73489,"type":"31-36","attributes_id":1197},{"id":73490,"type":"25-30","attributes_id":1197},{"id":73491,"type":"32E","attributes_id":1197},{"id":73492,"type":"32D","attributes_id":1197},{"id":73493,"type":"34E","attributes_id":1197},{"id":73494,"type":"36E","attributes_id":1197},{"id":73495,"type":"38E","attributes_id":1197},{"id":73496,"type":"30D","attributes_id":1197},{"id":73497,"type":"30E","attributes_id":1197},{"id":73498,"type":"42F","attributes_id":1197},{"id":73499,"type":"71","attributes_id":1197},{"id":73500,"type":"40E","attributes_id":1197},{"id":73501,"type":"3.5/4","attributes_id":1197},{"id":73502,"type":"5/5.5","attributes_id":1197},{"id":73503,"type":"6.5/7","attributes_id":1197},{"id":73504,"type":"10M","attributes_id":1197},{"id":73505,"type":"11M","attributes_id":1197},{"id":73506,"type":"28-32","attributes_id":1197},{"id":73507,"type":"28-34","attributes_id":1197},{"id":73508,"type":"29-30","attributes_id":1197},{"id":73509,"type":"29-32","attributes_id":1197},{"id":73510,"type":"29-34","attributes_id":1197},{"id":73511,"type":"31-30","attributes_id":1197},{"id":73512,"type":"31-32","attributes_id":1197},{"id":73513,"type":"31-34","attributes_id":1197},{"id":73514,"type":"41-42","attributes_id":1197},{"id":73515,"type":"43-44","attributes_id":1197}]},{"id":1198,"value":"Color","observation":"opcion","types":[{"id":73516,"type":"Amarillo","attributes_id":1198},{"id":73517,"type":"Amarillo claro","attributes_id":1198},{"id":73518,"type":"Amarillo Limón","attributes_id":1198},{"id":73519,"type":"Amarillo Topacio","attributes_id":1198},{"id":73520,"type":"Amatista","attributes_id":1198},{"id":73521,"type":"Ámbar","attributes_id":1198},{"id":73522,"type":"Azul","attributes_id":1198},{"id":73523,"type":"Azul Acero Claro","attributes_id":1198},{"id":73524,"type":"Azul Cobalto","attributes_id":1198},{"id":73525,"type":"Azul Francia","attributes_id":1198},{"id":73526,"type":"Azul Klein","attributes_id":1198},{"id":73527,"type":"Azul Marino","attributes_id":1198},{"id":73528,"type":"Azul Petróleo","attributes_id":1198},{"id":73529,"type":"Azul Prusia","attributes_id":1198},{"id":73530,"type":"Azul Turquí","attributes_id":1198},{"id":73531,"type":"Azul Zafiro","attributes_id":1198},{"id":73532,"type":"Beige","attributes_id":1198},{"id":73533,"type":"Bermellón","attributes_id":1198},{"id":73534,"type":"Blanco","attributes_id":1198},{"id":73535,"type":"Borgoña / Caoba","attributes_id":1198},{"id":73536,"type":"Burdeos","attributes_id":1198},{"id":73537,"type":"Café","attributes_id":1198},{"id":73538,"type":"Café Claro","attributes_id":1198},{"id":73539,"type":"Café Oscuro","attributes_id":1198},{"id":73540,"type":"Carmín","attributes_id":1198},{"id":73541,"type":"Celeste","attributes_id":1198},{"id":73542,"type":"Celeste Acero","attributes_id":1198},{"id":73543,"type":"Chocolate","attributes_id":1198},{"id":73544,"type":"Cian","attributes_id":1198},{"id":73545,"type":"Cian Oscuro","attributes_id":1198},{"id":73546,"type":"Cobre","attributes_id":1198},{"id":73547,"type":"Coral","attributes_id":1198},{"id":73548,"type":"Damasco","attributes_id":1198},{"id":73549,"type":"Dorado","attributes_id":1198},{"id":73550,"type":"Durazno","attributes_id":1198},{"id":73551,"type":"Esmeralda","attributes_id":1198},{"id":73552,"type":"Fucsia","attributes_id":1198},{"id":73553,"type":"Gris","attributes_id":1198},{"id":73554,"type":"Gris Azul Oscuro","attributes_id":1198},{"id":73555,"type":"Gris Claro","attributes_id":1198},{"id":73556,"type":"Gris Oscuro","attributes_id":1198},{"id":73557,"type":"Hueso","attributes_id":1198},{"id":73558,"type":"Índigo","attributes_id":1198},{"id":73559,"type":"Jade","attributes_id":1198},{"id":73560,"type":"khaki","attributes_id":1198},{"id":73561,"type":"Khaki Oscuro","attributes_id":1198},{"id":73562,"type":"Lavanda","attributes_id":1198},{"id":73563,"type":"Lavanda Floral","attributes_id":1198},{"id":73564,"type":"Lila","attributes_id":1198},{"id":73565,"type":"Lino","attributes_id":1198},{"id":73566,"type":"Magenta","attributes_id":1198},{"id":73567,"type":"Malva","attributes_id":1198},{"id":73568,"type":"Marfil","attributes_id":1198},{"id":73569,"type":"Marfil Claro","attributes_id":1198},{"id":73570,"type":"Menta","attributes_id":1198},{"id":73571,"type":"Morado","attributes_id":1198},{"id":73572,"type":"Naranjo","attributes_id":1198},{"id":73573,"type":"Naranjo Pálido","attributes_id":1198},{"id":73574,"type":"Negro","attributes_id":1198},{"id":73575,"type":"Negro Azabache","attributes_id":1198},{"id":73576,"type":"Negro Grafito","attributes_id":1198},{"id":73577,"type":"Negro Pizarra","attributes_id":1198},{"id":73578,"type":"Nieve","attributes_id":1198},{"id":73579,"type":"Ocre","attributes_id":1198},{"id":73580,"type":"Palo Rosa","attributes_id":1198},{"id":73581,"type":"Plateado","attributes_id":1198},{"id":73582,"type":"Púrpura","attributes_id":1198},{"id":73583,"type":"Púrpura Imperial","attributes_id":1198},{"id":73584,"type":"Rojo","attributes_id":1198},{"id":73585,"type":"Rojo Amaranto","attributes_id":1198},{"id":73586,"type":"Rojo Carmesí","attributes_id":1198},{"id":73587,"type":"Rojo Escarlata","attributes_id":1198},{"id":73588,"type":"Rojo Italiano","attributes_id":1198},{"id":73589,"type":"Rosa","attributes_id":1198},{"id":73590,"type":"Rosa fuerte","attributes_id":1198},{"id":73591,"type":"Rosa Oscuro","attributes_id":1198},{"id":73592,"type":"Siena","attributes_id":1198},{"id":73593,"type":"Siena Pálido","attributes_id":1198},{"id":73594,"type":"Turquesa","attributes_id":1198},{"id":73595,"type":"Verde","attributes_id":1198},{"id":73596,"type":"Verde Aguamarina","attributes_id":1198},{"id":73597,"type":"Verde Arlequín","attributes_id":1198},{"id":73598,"type":"Verde Espárrago","attributes_id":1198},{"id":73599,"type":"Verde Lima","attributes_id":1198},{"id":73600,"type":"Verde Mar","attributes_id":1198},{"id":73601,"type":"Verde Militar","attributes_id":1198},{"id":73602,"type":"Verde Oliva","attributes_id":1198},{"id":73603,"type":"Verde Pasto","attributes_id":1198},{"id":73604,"type":"Verde Veronés","attributes_id":1198},{"id":73605,"type":"Violeta","attributes_id":1198},{"id":73606,"type":"Violeta Oscuro","attributes_id":1198},{"id":73607,"type":"Zanahoria","attributes_id":1198},{"id":73608,"type":"Zinc","attributes_id":1198}]}]}}'.decode(
            "utf-8"))
    process_data(loads(data))


if __name__ == '__main__':
    main()
