from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import xlwt
import time


s=Service(ChromeDriverManager().install())

def login(driver):
    driver.get('https://www.mcmaster.com/')
    time.sleep(2)
    driver.find_element(By.ID,'LoginUsrCtrlWebPart_LoginLnk').click()
    time.sleep(1)
    driver.find_element(By.ID,'Email').send_keys('mapplecode2020@gmail.com')
    time.sleep(1)
    driver.find_element(By.ID,'Password').send_keys('kindle@123')
    time.sleep(1)
    driver.find_element(By.ID,'Password').send_keys(Keys.ENTER)
    time.sleep(2)
