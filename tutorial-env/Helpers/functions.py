from Helpers.constantes import USUARIO, PASSWORD, INITIAL_URL
from selenium.webdriver.common.by import By
from selenium import webdriver


def login():
    driver = webdriver.Chrome()
    driver.get(INITIAL_URL)
    username = driver.find_element(by=By.ID, value=USUARIO)
    username.send_keys(USUARIO)
    password = driver.find_element(by=By.ID, value=PASSWORD)
    password.send_keys(PASSWORD)
    driver.find_element(by=By.ID, value="login-button").click()
