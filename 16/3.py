import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

LINK = "https://suninjuly.github.io/huge_form.html"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    elements = driver.find_elements(By.CSS_SELECTOR, ".first_block input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

