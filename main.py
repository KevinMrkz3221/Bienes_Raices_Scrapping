from urllib3.packages.six import with_metaclass
from mainclass import *

def txt_to_list(document):
    paths = []
    with open(document, 'r') as f:
        for lines in f:
            paths.append(f.readlines())

    return paths    


if __name__ == '__main__':

    test = Clamudi()
    

    # Obtiene todo los objetos Solo utilizar cuando no tenemos elementos en nuestro archivo de texto ya que esto hace que tarde mas la ejecucion
    #test.list_of_links_by_page()
    #test.list_of_all_links()    
    #test.list_to_txt()

    #En caso de que se corrieran las lineas anteriores habla a estos metodos directamente
    paths = txt_to_list('./selenium_webElement.txt')
    test.auto_extraction(paths)

    test.tearDown()

