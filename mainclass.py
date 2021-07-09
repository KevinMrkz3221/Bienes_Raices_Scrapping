import unittest
from selenium import webdriver
import pandas as pd


class Clamudi(unittest.TestCase,):

    def __init__(self):
        #driver options
        """ 
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("-headless")
        self.options.add_argument("-no-sandbox")
        self.options.add_argument("-disable-dev-shm-usage")
         """
        #driver Init
        self.driver = webdriver.Chrome(options= None, executable_path='./chromedriver')
        self.driver.get("https://www.lamudi.com.mx/chihuahua/ciudad-juarez-2/casa/for-sale/?currency=mxn&page=0")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
    
    def setUp(self, path):
        self.driver.get(path)

    def switch_window(self, item):
        self.driver.switch_to.window(item)
    
    def list_of_links_by_page(self):
        self.links = self.driver.find_elements_by_link_text("Ver mas Info")
        href = [link.get_attribute('href') for link in self.links]
        self.links = href

    def next_page(self):
        self.driver.find_element_by_class_name("next").click()

    def list_of_all_links(self):
        links = []
        new_list = []
        for _ in range(20):
            self.list_of_links_by_page()
            links.append(self.links)
            self.next_page()
            
        for i in range(len(links)):
            for j in range(len(links[i])):
                new_list.append(links[i][j])
        
        self.links = new_list

    
    def list_to_txt(self):
        with open("selenium_webElement.txt", 'w') as f: 
            for element in self.links:
                f.write(str(element)+'\n')
        
    
    def extraction(self):
        details = self.driver.find_elements_by_class_name("columns-2")
        details = [detail.text for detail in details]
        price = self.driver.find_element_by_class_name("Overview-main")
        direction = self.driver.find_element_by_class_name("Header-title-address-text")
        description = self.driver.find_element_by_class_name("ViewMore-text-description")
        amenities = self.driver.find_elements_by_class_name("amenities-cols")
        amenities = [ameniti.text for ameniti in amenities]

        return description.text, amenities, details, price.text, direction.text

    def auto_extraction(self, paths):
        data = []
        paths_format = []
        for i in range(len(paths)):
            for j in range(len(paths[i])):
                paths_format.append(paths[i][j])

        paths = paths_format

         
        for path in paths:
            try:
                print(path)
                self.setUp(path)
                data.append(self.extraction())
            except:
                self.data = data
                df = pd.DataFrame(data, columns=["Descripcion","Amenidades","Detalles", "Precio", "Direccion"])
                df.to_csv('./BRdf.csv')
                pass
        
        self.data = data

        df = pd.DataFrame(data, columns=["Descripcion","Amenidades","Detalles", "Precio", "Direccion"])
        
        df.to_csv('./BRdf.csv')

    def tearDown(self):
        self.driver.quit()