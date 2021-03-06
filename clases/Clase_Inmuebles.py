from clases.Clase_Lamudi import *



class CInmuebles(Clamudi):
    def __init__(self, url):
        super().__init__(url)
        self.number_page = 0

    def list_of_links_by_page(self):
        try:
            self.driver.implicitly_wait(1)
            self.links = self.driver.find_elements_by_class_name("postingCard")
            href = ["https://www.inmuebles24.com"+link.get_attribute('data-to-posting') for link in self.links]
            self.links = href 
            self.number_page =+ self.number_page + 1   
        except:
            print("No data found")

    

    def next_page(self):
        path = "https://www.inmuebles24.com/casas-en-venta-en-juarez-pagina-{}".format(self.number_page)+".html"
        self.setOtherPage(path)

    def extraction(self):
        details = self.driver.find_elements_by_class_name("icon-feature")
        details = [detail.text for detail in details]
        price = self.driver.find_element_by_class_name("price-items")
        direction = self.driver.find_element_by_class_name("title-location")
        description = self.driver.find_element_by_id("longDescription")
        amenities = self.driver.find_elements_by_class_name("article-tabs-item")
        amenities = [ameniti.text for ameniti in amenities]

        return description.text, amenities, details, price.text, direction.text