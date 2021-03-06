from selenium import webdriver
import pandas as pd
from datetime import date
from os import chdir, getcwd
from tqdm.auto import tqdm
from selenium.webdriver.chrome.options import Options

class Cbase():
    def __init__(self, url):
            # driver options
            
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("-headless")
            self.options.add_argument("-no-sandbox")
            self.options.add_argument("-disable-dev-shm-usage")

            # inits de ayuda
            self.url = url
            self.main_dir = getcwd()
            self.chromedriver = self.main_dir + "/chromedriver"

    # driver Init
    def setUp(self, bool):
        if bool:        
            self.driver = webdriver.Chrome(options=None, executable_path=self.chromedriver)
            self.driver.get(self.url)
        else:
            self.driver = webdriver.Chrome(options=self.options, executable_path=self.chromedriver)
            self.driver.get(self.url)
        
        self.driver.maximize_window()           # Se maximiza para ver si no se encuentran elementos ocultos
        self.driver.implicitly_wait(15)         # Minimo va a esperar 15 segundos a que la pagina reaccione



    # cambia la pagina con la que se esta trabajando
    def setOtherPage(self, path):
        self.driver.get(path)

    # obtiene unicamente los enlaces de la pagina en la que se encuentra
    def list_of_links_by_page(self):
        pass

    # salta a la siguiente pagina si al final tiene un elemento Next
    def next_page(self):
        pass

    # busca las clases o los puntos de interes de nuestra pagina
    def extraction(self):
        pass


    # Obtiene todos los links de las paginas de interes y las guarda en una lista dentro de la clase
    def list_of_all_links(self,  No_Pages):
        links = []
        new_list = []
        self.driver.implicitly_wait(2)
        print("Getting links: ")
        for _ in tqdm(range(No_Pages)):
            try:
                self.list_of_links_by_page()
                links.append(self.links)
                self.next_page()
            except:
                pass

        for i in range(len(links)):  # Lista bidimensional a lista de 1 dimension
            for j in range(len(links[i])):
                new_list.append(links[i][j])

        result = []  # se eliminan elementos repetidos
        for item in new_list:
            if item not in result:
                result.append(item)

        self.links = result


    # Crea un archivo de texto que contiene todos los enlaces que nos interesan para una furuta extraccion
    def list_to_txt(self, name, path):  # agregar parametro de nombre de archivo
        
        save_dir =getcwd() + "/Selenium_webElements/{}".format(path)
        
        chdir(save_dir)

        with open("{}_webElement_{}.txt".format(name, date.today()), "w") as f:
            for element in self.links:
                f.write(str(element)+'\n')
        
        chdir(self.main_dir)

    
    # automatiza la extraccion de datos

    def auto_extraction(self, name, path):
        data = []
        save_dir = getcwd() + "/data/{}".format(path)
        self.driver.implicitly_wait(2)
        print("Getting data: ")
        chdir(save_dir)
        for link in tqdm(self.links):
            try:
                self.setOtherPage(link)
                data.append(self.extraction())
                #print(i, ": ", link, "\n\tTime: ", time() - start)
                df = pd.DataFrame(data, columns=["Descripcion", "Amenidades", "Detalles", "Precio", "Direccion"])
                
                df.to_csv("{}_{}.csv".format(name, date.today()))
                
            except:
                pass

        self.data = pd.DataFrame(data, columns=["Descripcion", "Amenidades", "Detalles", "Precio", "Direccion"])
        chdir(self.main_dir)
    def tearDown(self):
        self.driver.quit()
