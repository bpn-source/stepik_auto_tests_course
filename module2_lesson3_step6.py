import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.TAG_NAME, "input").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()
    print(browser.switch_to.alert.text)

finally:

    time.sleep(10)
    browser.quit()