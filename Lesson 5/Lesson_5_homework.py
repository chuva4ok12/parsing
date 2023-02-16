from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service('./geckodriver')
driver = webdriver.Firefox(service=s)

driver.get('https://www.mvideo.ru/')
time.sleep(10)
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
time.sleep(5)
button = driver.find_element(By.XPATH, '//button[@class="tab-button ng-star-inserted"]')
button.click()
products = driver.find_element(By.XPATH, "//mvid-carousel[@class='carusel ng-star-inserted']/"
                                          "div[@class='mvid-carousel-outer mv-hide-scrollbar']")
product_name = products.find_elements(By.XPATH, ".//div[@class='product-mini-card__name ng-star-inserted']"
                                                     "/div/a/div")
product_price = products.find_elements(By.XPATH, ".//div[@class='product-mini-card__price ng-star-inserted']"
                                                 "/mvid-price/div/span[@class='price__main-value']")
for i in range(len(product_name)):
    print(product_name[i].text)
    print(product_price[i].text)
driver.close()

