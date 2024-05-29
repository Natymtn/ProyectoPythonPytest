import pytest
from Helpers.functions import driver_ini, setup_data
from selenium.webdriver.common.by import By


def test_login(setup_data, driver_ini):
    driver = driver_ini
    driver.get((setup_data['url']))
    username = driver.find_element(by=By.ID, value="user-name")
    username.send_keys(setup_data['username'])
    password = driver.find_element(by=By.ID, value="password")
    password.send_keys(setup_data['password'])
    driver.find_element(by=By.ID, value="login-button").click()
    assert (setup_data['url'] != driver.current_url)
    driver.quit()
