import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os



try: 
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys('Имя')
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('Имя2')
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('Почта')
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()