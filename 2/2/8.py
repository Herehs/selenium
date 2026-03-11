import os
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

LINK = "https://suninjuly.github.io/file_input.html"



service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)

try:
    file_path = os.path.join(current_dir, '1.txt')
    print(file_path)

    driver.get(LINK)
    driver.implicitly_wait(3)

    firstName = driver.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(2)")
    firstName.send_keys("a")

    secondName = driver.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(4)")
    secondName.send_keys("a")

    email = driver.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(6)")
    email.send_keys("a")

    file = driver.find_element(By.CSS_SELECTOR, "#file")
    file.send_keys(file_path)

    time.sleep(2)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Число из алерта: {alert_text}")

finally:
    time.sleep(5)
    driver.quit()