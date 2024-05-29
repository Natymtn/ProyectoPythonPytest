import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helpers.functions import driver_ini,login,setup_data
import time


#Inicializacion del driver llamando el fixture driver_ini() y login()
def test_menu_inventory(driver_ini, login):
        btn_burger = WebDriverWait(driver_ini,5).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        btn_burger.click()
        driver_ini.find_element(by=By.ID, value="react-burger-cross-btn")
        #elementos del menu lateral
        driver_ini.find_element(by=By.ID, value="inventory_sidebar_link")
        driver_ini.find_element(by=By.ID, value="about_sidebar_link")
        driver_ini.find_element(by=By.ID, value="logout_sidebar_link")
        driver_ini.find_element(by=By.ID, value="reset_sidebar_link")
        driver_ini.quit()


def test_about_item(driver_ini, login):
        btn_burger = WebDriverWait(driver_ini, 5).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        btn_burger.click()
        driver_ini.find_element(by=By.ID, value="about_sidebar_link").click()
        driver_ini.quit()





#investigar como ejecutar distintos tests para verificar la aparición de los botones de cierre y opciones del men+u
#sin repetir_todo el proceso de login. Es una buena practica hacer muchos assert en un test?
#o deberia dividir varios test en una clase. En ese caso cómo hacer una función
#que se encuentre al inicio para que sea ocupada por los test de la clase
