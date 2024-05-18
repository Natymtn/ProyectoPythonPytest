import pytest
import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
initial_url="https://www.saucedemo.com/"

def test_login():
    driver.get(initial_url)
    title_login = driver.title
    username = driver.find_element(by=By.ID, value="user-name")
    username.send_keys('standard_user')
    password = driver.find_element(by=By.ID, value="password")
    password.send_keys("secret_sauce")
    driver.find_element(by=By.ID, value="login-button").click()
    driver.implicitly_wait(0.5)
    assert (initial_url != driver.current_url)
    driver.quit()

