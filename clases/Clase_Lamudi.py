from selenium import webdriver
import pandas as pd
from time import time
from datetime import date
from os import chdir


"""
    Atributos de la clase:

    Se crean inicialmente junto con el objeto:
        options
        driver

    Se crean al utilizar metodos:
        Links:  Se necesita utilizar la funcion list_of_links_by_page o list_of_all_links
        Data:   Se necesita utilizar la funcion auto_extraction

"""


class Clamudi():

    def __init__(self):
        # driver options
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("-headless")
        self.options.add_argument("-no-sandbox")
        self.options.add_argument("-disable-dev-shm-usage")

        # driver Init
        self.driver = webdriver.Chrome(options=self.options, executable_path='./chromedriver')
        self.driver.get("https://www.lamudi.com.mx/chihuahua/ciudad-juarez-2/casa/for-sale/?currency=mxn&page=1")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    # cambia la pagina con la que se esta trabajando
    def setUp(self, path):
        self.driver.get(path)

    def switch_window(self, item):
        self.driver.switch_to.window(item)

    # obtiene unicamente los enlaces de la pagina en la que se encuentra

    def list_of_links_by_page(self):
        self.links = self.driver.find_elements_by_link_text("Ver mas Info")
        href = [link.get_attribute('href') for link in self.links]
        self.links = href

    # salga a la siguiente pagina si al final tiene un elemento Next
    def next_page(self):
        self.driver.find_element_by_class_name("next").click()

    # Obtiene todos los links de las paginas de interes y las guarda en una lista dentro de la clase
    def list_of_all_links(self,  No_Pages):
        start = time()
        links = []
        new_list = []

        for _ in range(No_Pages):
            self.list_of_links_by_page()
            links.append(self.links)
            self.next_page()

        for i in range(len(links)):  # Lista bidimensional a lista de 1 dimension
            for j in range(len(links[i])):
                new_list.append(links[i][j])

        result = []  # se eliminan elementos repetidos
        for item in new_list:
            if item not in result:
                result.append(item)

        self.links = result

        print("List of all links Execution time: ", time() - start)

    # Crea un archivo de texto que contiene todos los enlaces que nos interesan para una furuta extraccion
    def list_to_txt(self, name):  # agregar parametro de nombre de archivo
        start = time()
        chdir("/home/kevin/Documents/IA Center/scrap_bienes_raices/Selenium_webElements")
        with open("./{}_webElement_{}.txt".format(name, date.today()), "w") as f:
            for element in self.links:
                f.write(str(element)+'\n')

        print("List to text Execution Time:", time() - start)

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

    # automatiza la extraccion de datos

    def auto_extraction(self, name):
        data = []

        i = 0  # Se utiliza como contador para mostrar en que elemento va

        for link in self.links:
            try:
                i += 1
                start = time()
                self.setUp(link)
                data.append(self.extraction())
                print(i, ": ", link, "\n\tTime: ", time() - start)
                df = pd.DataFrame(data, columns=["Descripcion", "Amenidades", "Detalles", "Precio", "Direccion"])
                df.to_csv("../data/{}_{}.csv".format(name, date.today()))

            except:
                print("pass")

        self.data = pd.DataFrame(data, columns=["Descripcion", "Amenidades", "Detalles", "Precio", "Direccion"])

    def tearDown(self):
        self.driver.quit()
