import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get("https://www.cartadeivinicdv.com/account/login?return_url=%2Faccount")

def login():
    driver.find_element('xpath', '//*[@id="CustomerEmail"]').send_keys("shiryu.cavaleiro73@gmail.com")
    driver.find_element('xpath', '//*[@id="CustomerPassword"]').send_keys("123456")
    driver.find_element('xpath', '//*[@id="customer_login"]/input[3]').click()



login()