import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

LINK = "https://SunInJuly.github.io/execute_script.html"


# Функция для вычисления математического выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Значение x: {x}")

    y = calc(x)
    print(f"Результат вычислений: {y}")



    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_radio = driver.find_element(By.CSS_SELECTOR, "div.form-check:nth-child(4) > label:nth-child(2)")
    driver.execute_script("return arguments[0].scrollIntoView(true);", robots_radio)
    robots_radio.click()

    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)

    button.click()

    time.sleep(2)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Число из алерта: {alert_text}")

finally:
    time.sleep(5)
    driver.quit()