from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.cartadeivinicdv.com/products/andre-clouet-un-jour-de-1911-grand-cru-brut?variant=37853625417877")
print(driver.title)

driver.quit()