import os

import time
import math


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


LINK = "https://suninjuly.github.io/explicit_wait2.html"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )

    book = driver.find_element(By.CSS_SELECTOR, "#book")
    book.click()

    number = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    print(number)

    textField = driver.find_element(By.CSS_SELECTOR, "#answer")
    textField.send_keys(calc(number))

    submit_button = driver.find_element(By.CSS_SELECTOR, "#solve")
    submit_button.click()

    time.sleep(2)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Число из алерта: {alert_text}")

finally:
    time.sleep(5)
    driver.quit()