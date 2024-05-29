import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Helpers.constantes import USUARIO, PASSWORD

driver = webdriver.Chrome()
initial_url="https://www.saucedemo.com/"

def test_login():
    driver.get(initial_url)
    username = driver.find_element(by=By.ID, value="user-name")
    username.send_keys(USUARIO)
    password = driver.find_element(by=By.ID, value="password")
    password.send_keys(PASSWORD)
    driver.find_element(by=By.ID, value="login-button").click()
    assert (initial_url != driver.current_url)
    driver.quit()



