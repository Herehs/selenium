from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
import math

LINK = "https://suninjuly.github.io/find_link_text"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    link.click()

    value1 = "input"
    value2 = "last_name"
    value3 = ".form-control.city"
    input1 = driver.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, value2)
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CSS_SELECTOR, value3)
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    driver.quit()
