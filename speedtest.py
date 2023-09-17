from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By

import time
import csv
import datetime
 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# fast.comを開いてshow-more-details-linkが現れるまで最大20秒待機
# 現れなかったらエラーをCSVに書き込む
driver.get('https://fast.com/ja/')
try:
    
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'show-more-details-link')))

except TimeoutException as te:

    csv_path =  r"out.csv"
    day = datetime.date.today()
    activetime = datetime.datetime.now().strftime('%H:%M:%S')
    
    list_data = []
    list_data.append(day)
    list_data.append(activetime)
    list_data.append("error")

    with open(csv_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list_data)

    driver.close()
    driver.quit()

# fast.comの詳細を表示をクリックして30秒待機
details_link = driver.find_element(By.ID,'show-more-details-link')
details_link.click()
time.sleep(30)

# 必要な要素を取得する
dowloadspeed_units = str(driver.find_element(By.ID,'speed-units').text)
downloadspeed_value = str(driver.find_element(By.ID,'speed-value').text)
latency_value = str(driver.find_element(By.ID,'latency-value').text)
bufferbloat_value = str(driver.find_element(By.ID,'bufferbloat-value').text)
user_ip = str(driver.find_element(By.XPATH,'//*[@id="user-ip"]').text)
upload_units = str(driver.find_element(By.ID,'upload-units').text)
upload_value = str(driver.find_element(By.ID,'upload-value').text)

# 取得日時を変数に入れる
day = datetime.date.today()
activetime = datetime.datetime.now().strftime('%H:%M:%S')

# リストに上記を入れる
list_data = []
list_data.append(day)
list_data.append(activetime)
list_data.append(user_ip)
list_data.append(downloadspeed_value)
list_data.append(dowloadspeed_units)
list_data.append(upload_value)
list_data.append(upload_units)
list_data.append(latency_value)
list_data.append(bufferbloat_value)

print(list_data)

# CSV出力
csv_path =  r"out.csv"
with open(csv_path, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list_data)

# driverの終了
driver.close()
driver.quit()


