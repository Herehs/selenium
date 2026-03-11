import math
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

LINK = "http://suninjuly.github.io/get_attribute.html"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    image = driver.find_element(By.CSS_SELECTOR, "#treasure")
    valx = float(image.get_attribute("valuex"))

    answer = driver.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(str(math.log(abs(12 * math.sin(valx)), math.exp(1))))

    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robots_rule = driver.find_element(By.ID, "robotsRule")
    robots_rule.click()
finally:
    submit = driver.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    submit.click()
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()


