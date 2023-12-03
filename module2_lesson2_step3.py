import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    total = str(int(num1.text) + int(num2.text))
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(total)
    
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()