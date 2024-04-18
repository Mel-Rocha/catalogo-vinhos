from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def extract_wine():
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.cartadeivinicdv.com/collections/cdv-selection/products/bd-n-brut-nature-bourgeois-diaz?variant=40284299755669")

        produttore_element = driver.find_element('xpath', '//*[@id="description-main"]/div/div/div/p')
        produttore = produttore_element.text
        print("Produttore:", produttore)

    finally:
        driver.quit()

extract_wine()
