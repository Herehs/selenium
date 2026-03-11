import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

LINK = "https://suninjuly.github.io/selects2.html"

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get(LINK)
    driver.implicitly_wait(3)

    # Находим числа и вычисляем сумму
    num1 = int(driver.find_element(By.ID, "num1").text)
    num2 = int(driver.find_element(By.ID, "num2").text)
    result = num1 + num2
    print(f"Число 1: {num1}, Число 2: {num2}, Сумма: {result}")

    # Работаем с выпадающим списком
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))  # Выбираем значение по сумме

    # Нажимаем кнопку Submit
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    # Ждем появления алерта и получаем число
    time.sleep(2)  # Небольшая задержка для загрузки алерта
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Число из алерта: {alert_text}")

    # Принимаем алерт
    alert.accept()

finally:
    time.sleep(30)
    driver.quit()




