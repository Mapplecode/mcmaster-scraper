from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import xlwt
import time
wb = xlwt.Workbook()
ws = wb.add_sheet('Categories')
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get('https://www.mcmaster.com/')
time.sleep(5)
categories = driver.find_element(By.ID,'HomePageNavigation').find_elements(By.TAG_NAME,'a')

categories_list = list()
for cat in categories:
    try:
        print(cat.text,cat.get_attribute('href'))
        categories_list.append({'name':str(cat.text),'href':str(cat.get_attribute('href'))})

    except Exception as e:
        pass
ws.write(0, 0, 'No')
ws.write(0, 1,'NAME')
ws.write(0, 2,'link')
count = 1
for data in categories_list:
    ws.write(count, 0, count)
    ws.write(count, 1,data.get('name'))
    ws.write(count, 2, data.get('href'))
    count = count + 1
wb.save('categories.xls')
driver.quit()