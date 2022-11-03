import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("C:\\Users\\rafae\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get('https://www.sefaz.salvador.ba.gov.br/Iptu/certidaoDadosCadastrais?Length=4#gsc.tab=0');

time.sleep(5) # Let the user actually see something!
#clickable = driver.find_element("//html/body/form/div[3]/div/div[3]/div[1]/div[1]/input")
clickable = driver.find_element("//html/body/form/div[3]/div/div[3]/div[1]/div[1]/input")
ActionChains(driver).click_and_hold(clickable).perform()
input=webdriver.Chrome.find_element('//*[@id="ctl00_ContentPlaceHolderPrincipal_txtCdInscricao"]')
input.send_keys("Python")
time.sleep(5) # Let the user actually see something!



driver 