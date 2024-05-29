import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


@pytest.fixture()
def setup_data():
    data = {'username': 'standard_user', 'password': 'secret_sauce', 'url': 'https://www.saucedemo.com/'}
    return data


@pytest.fixture()
def driver_ini():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def login(setup_data, driver_ini):
    time.sleep(3)
    driver = driver_ini
    driver.get((setup_data['url']))
    username = driver.find_element(by=By.ID, value="user-name")
    username.send_keys(setup_data['username'])
    password = driver.find_element(by=By.ID, value="password")
    password.send_keys(setup_data['password'])
    driver.find_element(by=By.ID, value="login-button").click()



