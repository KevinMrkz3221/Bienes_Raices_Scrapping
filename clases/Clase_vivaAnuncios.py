from Clase_Lamudi import *


class CViva_Anuncios(Clamudi):
    def __init__(self):
        #driver options
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("-headless")
        self.options.add_argument("-no-sandbox")
        self.options.add_argument("-disable-dev-shm-usage")
        
        #driver Init
        self.driver = webdriver.Chrome(options= self.options, executable_path='./chromedriver')
        self.driver.get("https://www.vivanuncios.com.mx/s-venta-inmuebles/juarez/v1c1097l10185p1")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)


    def list_of_links_by_page(self):
        pass

    def next_page(self):
        pass

    def extraction(self):
        pass