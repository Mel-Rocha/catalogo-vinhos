from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def extract_max(url):
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        result = {}
        elements = driver.find_elements(By.XPATH, "//div[@data-mce-fragment='1']")
        for element in elements:
            text = element.text

            result[element.get_attribute('id')] = text

        return result

    finally:
        driver.quit()


url = "https://www.cartadeivinicdv.com/products/andre-clouet-un-jour-de-1911-grand-cru-brut?variant=37853625417877"
result = extract_max(url)
print(result)
