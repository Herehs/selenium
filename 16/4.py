import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

LINK = "http://suninjuly.github.io/find_xpath_form"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    elements = driver.find_elements(By.CSS_SELECTOR, ".form-group input")
    for element in elements:
        element.send_keys("Мой ответ")


    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    driver.quit()

