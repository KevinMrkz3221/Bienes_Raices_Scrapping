
from selenium import webdriver
import pandas as pd
from time import time
from datetime import date
import os


class Clamudi():

    def __init__(self):
        #driver options
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("-headless")
        self.options.add_argument("-no-sandbox")
        self.options.add_argument("-disable-dev-shm-usage")
        
        #driver Init
        self.driver = webdriver.Chrome(options= self.options, executable_path='./chromedriver')
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
        start = time()
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
        print("List of all links Execution time: ",time() - start)
    
    def list_to_txt(self):
        start = time()
        os.chdir("/home/kevin/Documents/IA Center/scrap_bienes_raices/Selenium_webElements")
        with open("./selenium_webElement_{}.txt".format(date.today()), "w") as f: 
            for element in self.links:
                f.write(str(element)+'\n')

            
        print("List to text Execution Time:",time() - start)
        
    
    def extraction(self):
        details = self.driver.find_elements_by_class_name("columns-2")
        details = [detail.text for detail in details]
        price = self.driver.find_element_by_class_name("Overview-main")
        direction = self.driver.find_element_by_class_name("Header-title-address-text")
        description = self.driver.find_element_by_class_name("ViewMore-text-description")
        amenities = self.driver.find_elements_by_class_name("amenities-cols")
        amenities = [ameniti.text for ameniti in amenities]

        return description.text, amenities, details, price.text, direction.text

    def auto_extraction(self):
        data = []
        
        i = 0 #Se utiliza como contador para mostrar en que elemento va
         
        for link in self.links:
            try:
                i += 1 
                start = time()
                self.setUp(link)
                data.append(self.extraction())
                self.driver.implicitly_wait(2)
                print(i,": ",link, "Time: ", time() - start)
                
                df = pd.DataFrame(data, columns=["Descripcion","Amenidades","Detalles", "Precio", "Direccion"])
                df.to_csv("../data/Clamundi_{}.csv".format(date.today()))

            except:
                pass
        
        
        self.data = pd.DataFrame(data, columns=["Descripcion","Amenidades","Detalles", "Precio", "Direccion"])

        
    def tearDown(self):
        self.driver.quit()