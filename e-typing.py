from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

# URLだ 飛ぶぞ
# IT用語用
# url='https://www.e-typing.ne.jp/roma/variety/business.asp'

# 普通用
url = 'https://www.e-typing.ne.jp/roma/check/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

# 今すぐチェック

# IT用語用
# driver.find_element(By.XPATH, "//a[contains(@title,'IT用語')]").click()

# 普通用
driver.find_element(By.CLASS_NAME,'edro').click()
time.sleep(1)

# modal
wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.ID, "typing_content")))
time.sleep(1)
frame2 = driver.find_element(By.XPATH, "//iframe[@id='typing_content']")
driver.switch_to.frame(frame2)
driver.find_element(By.ID, 'start_btn').click()

# game start
body_element = driver.find_element(By.TAG_NAME,'body')
body_element.send_keys(Keys.SPACE)
time.sleep(3.5)

while True:
    try:
        sentences = driver.find_element(By.XPATH, '//div[@id="sentenceText"]').text
        for sentence in sentences:
            # 引数に入れたキーを打ってくれるやつ
            driver.find_element(By.TAG_NAME, "body").send_keys(sentence)
        time.sleep(0.25)
    except:
        break

time.sleep(20)