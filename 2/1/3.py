import math
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

LINK = "https://suninjuly.github.io/math.html"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))

    input = driver.find_element(By.ID, "answer")
    input.send_keys(y)

    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule = driver.find_element(By.ID, "robotsRule")
    robots_rule.click()

    submit = driver.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()


