from clases.Clase_Base import *

"""
    Atributos de la clase:

    Se crean inicialmente junto con el objeto:
        options
        driver

    Se crean al utilizar metodos:
        Links:  Se necesita utilizar la funcion list_of_links_by_page o list_of_all_links
        Data:   Se necesita utilizar la funcion auto_extraction

"""


class Clamudi(Cbase):

    def __init__(self, url):
        super().__init__(url)

    # obtiene unicamente los enlaces de la pagina en la que se encuentra
    def list_of_links_by_page(self):
        self.links = self.driver.find_elements_by_link_text("Ver mas Info")
        href = [link.get_attribute('href') for link in self.links]
        self.links = href

    # salga a la siguiente pagina si al final tiene un elemento Next
    def next_page(self):
        self.driver.find_element_by_class_name("next").click()

    # busca las clases o los puntos de intere de nuestra pagina
    def extraction(self):
        details = self.driver.find_elements_by_class_name("columns-2")
        details = [detail.text for detail in details]
        price = self.driver.find_element_by_class_name("Overview-main")
        direction = self.driver.find_element_by_class_name("Header-title-address-text")
        description = self.driver.find_element_by_class_name("ViewMore-text-description")
        amenities = self.driver.find_elements_by_class_name("amenities-cols")
        amenities = [ameniti.text for ameniti in amenities]

        return description.text, amenities, details, price.text, direction.text

