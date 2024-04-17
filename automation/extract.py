from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup, NavigableString


def extract_wine(url):
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

    def extract_min(url):
        response = requests.get(url)
        response_content = response.text

        soup = BeautifulSoup(response_content, 'html.parser')

        strongs = soup.find_all('strong')

        result = {}

        for strong in strongs:
            key = strong.get_text(strip=True)
            if key in ["NOTE DI DEGUSTAZIONE", "PRODUTTORE"]:
                next_sibling = strong.next_sibling
                if isinstance(next_sibling, NavigableString):
                    value = next_sibling.strip()
                elif next_sibling is not None:
                    value = next_sibling.get_text(strip=True)
                else:
                    value = None
                result[key] = value

        return result

    result_max = extract_max(url)
    result_min = extract_min(url)


    return result_max, result_min

url = "https://www.cartadeivinicdv.com/products/coorvieto-classico-superiore-2009-castello-di-corbara?variant=40341213544597"
result_max, result_min = extract_wine(url)
print("Resultados de extract_max:")
print(result_max)
print("\nResultados de extract_min:")
print(result_min)
