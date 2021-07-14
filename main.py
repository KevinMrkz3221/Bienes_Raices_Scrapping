
from clases.Clase_Lamudi import *

def txt_to_list(document):
    paths = []
    with open(document, 'r') as f:
        for lines in f:
            paths.append(f.readlines())

    return paths    

def get_data_from_Clamudi():
    start = time()
    print("=====Obteniendo informacion de Lamudi=====")
    lamudi = Clamudi()                                #Crea nuestro objeto de extraccion

    lamudi.list_of_all_links()                        #genera una lista de elementos que contienen la direccion de la pagina web donde se extraera todo
    lamudi.list_to_txt()                              #Combierte la lista anterior a un archivo de texto en caso de que se requieran
    
    lamudi.auto_extraction()                          #Inicia la extraccion automatica de nuestro sitio web

    lamudi.tearDown()                                 #Cierra el driver del navegador

    print("Fin\n Tiempo de ejecucion: ",time() -  start/60)                            #Nos muestra el tiempo de ejecucion de toda esta funcion

if __name__ == '__main__':

    get_data_from_Clamudi()
    


    

