from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


url='https://www.e-typing.ne.jp/roma/check/'
driver = webdriver.Chrome()
driver.get(url)

# 今すぐチェック
driver.find_element(By.CLASS_NAME,'edro').click()
time.sleep(2)

# modal
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, "typing_content")))
time.sleep(2)
frame2 = driver.find_element(By.XPATH, "//iframe[@id='typing_content']")
time.sleep(2)
print(frame2)
driver.switch_to.frame(frame2)
time.sleep(3)
driver.find_element(By.ID, 'start_btn').click()
print("click start_btn")
time.sleep(3)


body_element = driver.find_element(By.TAG_NAME,'body')
body_element.send_keys(Keys.SPACE)
time.sleep(3.5)

  