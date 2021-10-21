import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import xlwt
import xlrd
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
ua = UserAgent()
wb = xlwt.Workbook()
ws = wb.add_sheet('Categories')
s=Service(ChromeDriverManager().install())
opts = Options()
opts.add_argument("--enable-javascript")
opts.add_argument("user-agent={}".format(str(ua)))
driver = webdriver.Chrome(service=s,options=opts)
from login import login
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver.maximize_window()
driver.get('https://www.mcmaster.com/')

time.sleep(3)
try:
    login(driver)
except Exception as e:
    print(e)
#
# book = xlrd.open_workbook("sub-categories.xls")
# sh = book.sheet_by_index(0)
# for rx in range(1,sh.nrows):
#     link = str(sh.cell_value(rx,3))
#     print(requests.get(link).content)
#     time.sleep(3)
#     # link = link.replace('https://www.mcmaster.com/','')
#     # input_ = driver.find_element(By.ID,'SrchEntryWebPart_InpBox')
#     # input_.clear()
#     # input_.send_keys(link)
#     # input_.send_keys(Keys.ENTER)


time.sleep(30)