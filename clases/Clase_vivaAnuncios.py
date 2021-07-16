from clases.Clase_Lamudi import *


class CViva_Anuncios(Clamudi):
    def __init__(self, url):
        super().__init__(url)

    def list_of_links_by_page(self):
        self.links = self.driver.find_elements_by_class_name("href-link")
        href = [link.get_attribute('href') for link in self.links]
        self.links = href

    def next_page(self):
        try:
            self.driver.find_element_by_class_name(
                "icon-pagination-right").click()
        except:
            pass

    def extraction(self):
        details = self.driver.find_elements_by_class_name("category")
        details = [detail.text for detail in details]
        price = self.driver.find_element_by_class_name("ad-price")
        direction = self.driver.find_element_by_class_name("location-name")
        description = self.driver.find_element_by_class_name("description-content")
        amenities = self.driver.find_elements_by_class_name("amenities-chips")
        amenities = [ameniti.text for ameniti in amenities]

        return description.text, amenities, details, price.text, direction.text
