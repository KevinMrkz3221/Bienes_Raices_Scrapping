from functions import *

if __name__ == '__main__':
    # se habla a extractor de Lamudi
    #get_data_from_Clamudi("CLamudi")

    #Se habla a extractor de Viva Anuncios
    #get_data_from_VivaAnuncios("CVivaAnuncios")
    test = CInmuebles24()
    test.list_of_links_by_page()
    test.next_page()
    print(test.links[0])

    test.list_of_links_by_page()
    test.next_page()
    print(test.links[0])

    test.list_of_links_by_page()
    test.next_page()
    print(test.links[0])
    test.tearDown()

