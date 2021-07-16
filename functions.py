from clases.Clase_Lamudi import Clamudi
from clases.Clase_vivaAnuncios import CViva_Anuncios
from clases.Clase_Inmuebles import CInmuebles
from time import time

def txt_to_list(document):
    paths = []
    with open(document, 'r') as f:
        for lines in f:
            paths.append(f.readlines())

    return paths


def get_data_from_Clamudi(FileName, no_pages):
    start = time()
    path = "Lamudi"
    url = "https://www.lamudi.com.mx/chihuahua/ciudad-juarez-2/casa/for-sale/?currency=mxn&page=1"

    print("=====Obteniendo informacion de Lamudi=====")
    # Crea nuestro objeto de extraccion
    lamudi = Clamudi(url)         
    # Se define como se utilizara el driver si lo quieres ver o no True para ver de lo contrario False
    lamudi.setUp(False)             
    # genera una lista de elementos que contienen la direccion de la pagina web donde se extraera todo
    lamudi.list_of_all_links(no_pages)
    # Combierte la lista anterior a un archivo de texto en caso de que se requieran
    lamudi.list_to_txt(FileName, path)
    # Inicia la extraccion automatica de nuestro sitio web
    lamudi.auto_extraction(FileName, path)
    lamudi.tearDown()                       # Cierra el driver del navegador

    # Nos muestra el tiempo de ejecucion de toda esta funcion
    print("Fin\n Tiempo de ejecucion: ", (time() - start)/60)


def get_data_from_VivaAnuncios(FileName, no_pages):
    start = time()
    path = "VivaAnuncios"
    url = "https://www.vivanuncios.com.mx/s-venta-inmuebles/juarez/v1c1097l10185p1"

    print("=====Obteniendo informacion de Viva Anuncios=====")
    # Crea nuestro objeto de extraccion
    VivaAnuncios = CViva_Anuncios(url)        
    # Se define como se utilizara el driver si lo quieres ver o no True para ver de lo contrario False
    VivaAnuncios.setUp(False)   
    # genera una lista de elementos que contienen la direccion de la pagina web donde se extraera todo
    VivaAnuncios.list_of_all_links(no_pages)
    # Combierte la lista anterior a un archivo de texto en caso de que se requieran
    VivaAnuncios.list_to_txt(FileName, path)
    # Inicia la extraccion automatica de nuestro sitio web
    VivaAnuncios.auto_extraction(FileName, path)
    VivaAnuncios.tearDown()                 # Cierra el driver del navegador

    # Nos muestra el tiempo de ejecucion de toda esta funcion
    print("Fin\n Tiempo de ejecucion: ", (time() - start)/60)



def get_data_from_Inmuebles24(FileName, no_pages):
    start = time()
    path = "Inmuebles24"
    url = "https://www.inmuebles24.com/casas-en-venta-en-juarez.html#"

    print("=====Obteniendo informacion de Inmuebles24=====")
    # Crea nuestro objeto de extraccion
    Inmuebles = CInmuebles(url)         
    # Por el tipo de pagina es necesario marcar como True
    Inmuebles.setUp(True)  
    # genera una lista de elementos que contienen la direccion de la pagina web donde se extraera todo
    Inmuebles.list_of_all_links(no_pages)
    # Combierte la lista anterior a un archivo de texto en caso de que se requieran
    Inmuebles.list_to_txt(FileName, path)
    # Inicia la extraccion automatica de nuestro sitio web
    Inmuebles.auto_extraction(FileName, path)
    Inmuebles.tearDown()                 # Cierra el driver del navegador

    # Nos muestra el tiempo de ejecucion de toda esta funcion
    print("Fin\n Tiempo de ejecucion: ", (time() - start)/60)

