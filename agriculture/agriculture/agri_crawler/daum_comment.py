from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/thdwlsgus0/Desktop/chromedriver_win32/chromedriver.exe')
#driver = webdriver.PhantomJS('C:/Users/thdwlsgus0/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.implicitly_wait(3)
driver.get('https://logins.daum.net/accounts/loginform.do?')
driver.find_element_by_name('id').send_keys('thdwlsgus10')
driver.find_element_by_name('pw').send_keys('operwhe123!')
driver.find_element_by_xpath("//button[@class='btn_comm']").click()