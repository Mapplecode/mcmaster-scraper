from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import xlwt
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
ua = UserAgent()
wb = xlwt.Workbook()
ws = wb.add_sheet('Categories')
s=Service(ChromeDriverManager().install())
opts = Options()
opts.add_argument("user-agent={}".format(str(ua)))
driver = webdriver.Chrome(service=s,options=opts)
from login import login


driver.maximize_window()
time.sleep(5)
try:
    login(driver)
    print('USER LOGGED IN')
except Exception as e:
    print(e)
time.sleep(2)
categories = driver.find_element(By.ID,'HomePageNavigation').find_elements(By.TAG_NAME,'a')
ws.write(0, 0, 'No')
ws.write(0, 1,'Product Name')
ws.write(0, 2,'Sub-Category')
ws.write(0, 3,'Product link')
ws.write(0, 4,'Category Name')
ws.write(0, 5,'Category link')
count = 1
categories_list = list()
id_list = list()
li_list = list()
for cat in categories:
    try:
        # print(cat.text,cat.get_attribute('id'))
        id_list.append({'id':str(cat.get_attribute('id')),'name':cat.text,'link':str(cat.get_attribute('href'))})

    except Exception as e:
        print(e)

for cat in id_list:
    try:
        driver.find_element(By.ID,cat.get('id')).click()
        time.sleep(1)
        homepage = driver.find_element(By.ID,'HomePage')
        # print(homepage.text)
        subcat = homepage.find_elements(By.CLASS_NAME,'subcat')
        driver1 = driver.current_window_handle
        driver.switch_to.new_window()
        driver2 = driver.current_window_handle

        for sbc in subcat:
            header = sbc.find_element(By.TAG_NAME,'h2').text
            lis = sbc.find_elements(By.TAG_NAME,'a')
            for li in lis:
                if li.text == '':
                    continue
                print(li.text)
                driver.switch_to.window(driver2)
                driver.get(li.get_attribute('href'))
                time.sleep(4)
                driver.switch_to.window(driver1)
                time.sleep(2)
                # ws.write(count, 0, count)
                # ws.write(count, 1, li.text)
                # ws.write(count, 2, header)
                # ws.write(count, 3, li.get_attribute('href'))
                # ws.write(count, 4, cat.get('name'))
                # ws.write(count, 5, cat.get('href'))
                # count = count + 1
        # time.sleep(2)
    except Exception as e:
        print(e)
# wb.save('sub-categories.xls')
driver.quit()