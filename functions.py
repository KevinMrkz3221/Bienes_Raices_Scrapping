from clases.Clase_Lamudi import *
from clases.Clase_vivaAnuncios import CViva_Anuncios
from clases.Clase_Inmuebles import CInmuebles


def txt_to_list(document):
    paths = []
    with open(document, 'r') as f:
        for lines in f:
            paths.append(f.readlines())

    return paths


def get_data_from_Clamudi(FileName):
    start = time()
    print("=====Obteniendo informacion de Lamudi=====")
    # Crea nuestro objeto de extraccion
    lamudi = Clamudi()                      
    # genera una lista de elementos que contienen la direccion de la pagina web donde se extraera todo
    lamudi.list_of_all_links(20)
    # Combierte la lista anterior a un archivo de texto en caso de que se requieran
    lamudi.list_to_txt(FileName)
    # Inicia la extraccion automatica de nuestro sitio web
    lamudi.auto_extraction(FileName)
    lamudi.tearDown()                       # Cierra el driver del navegador

    # Nos muestra el tiempo de ejecucion de toda esta funcion
    print("Fin\n Tiempo de ejecucion: ", (time() - start)/60)


def get_data_from_VivaAnuncios(FileName):
    start = time()
    print("=====Obteniendo informacion de Viva Anuncios=====")
    # Crea nuestro objeto de extraccion
    VivaAnuncios = CViva_Anuncios()         
    # genera una lista de elementos que contienen la direccion de la pagina web donde se extraera todo
    VivaAnuncios.list_of_all_links(49)
    # Combierte la lista anterior a un archivo de texto en caso de que se requieran
    VivaAnuncios.list_to_txt(FileName)
    # Inicia la extraccion automatica de nuestro sitio web
    VivaAnuncios.auto_extraction(FileName)
    VivaAnuncios.tearDown()                 # Cierra el driver del navegador

    # Nos muestra el tiempo de ejecucion de toda esta funcion
    print("Fin\n Tiempo de ejecucion: ", (time() - start)/60)



def get_data_from_Inmuebles24(FileName):
    start = time()
    print("=====Obteniendo informacion de Inmuebles24=====")
    # Crea nuestro objeto de extraccion
    Inmuebles = CInmuebles()         
    # genera una lista de elementos que contienen la direccion de la pagina web donde se extraera todo
    Inmuebles.list_of_all_links(10)
    # Combierte la lista anterior a un archivo de texto en caso de que se requieran
    Inmuebles.list_to_txt(FileName)
    # Inicia la extraccion automatica de nuestro sitio web
    Inmuebles.auto_extraction(FileName)
    Inmuebles.tearDown()                 # Cierra el driver del navegador

    # Nos muestra el tiempo de ejecucion de toda esta funcion
    print("Fin\n Tiempo de ejecucion: ", (time() - start)/60)

