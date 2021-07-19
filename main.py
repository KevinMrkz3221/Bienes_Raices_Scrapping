
from functions import *

"""
    Para obtener informacion de Lamudi unicamente en main llamar la funcion
    get_data_from_lamudi("Aqui va nombre de archivo", no_pages)
    La variable no_pages cambia dependiendo la funcion ya que se le asigno el valaor por defecto 

    Se hace lo mismo para los otros sitios.

    Funciones activas por el momento:
        get_data_from_lamudi()
        get_data_from_VivaAnuncios()
        get_data_from_Inmuebles24()
"""

if __name__ == '__main__':
    get_data_from_Clamudi("Lamudi")
    get_data_from_VivaAnuncios("VivaAnuncios")
    get_data_from_Inmuebles24("Inmuebles24")