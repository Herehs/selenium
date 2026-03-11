import os

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


LINK = "http://suninjuly.github.io/redirect_accept.html"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    troll = driver.find_element(By.CSS_SELECTOR, ".trollface")
    troll.click()

    driver.switch_to.window(driver.window_handles[1])

    number = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    print(number)

    textField = driver.find_element(By.CSS_SELECTOR, "#answer")
    textField.send_keys(calc(number))

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

    time.sleep(2)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Число из алерта: {alert_text}")

finally:
    time.sleep(5)
    driver.quit()