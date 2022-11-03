import json
import time
import numpy as np
import pandas as pd
import pdfkit 
import requests
import xlrd
import codecs
import os
from datetime import date
from urllib import request
from lib2to3.pgen2.driver import Driver
from webbrowser import Chrome
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pywebcopy import save_webpage

#import webdriver
driver = webdriver.Chrome("C:\\Users\\rafae\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
# Acessa o site
driver.get("https://dti.sefaz.salvador.ba.gov.br/Modulos/DTI/ItivDeclaracaoFrm.aspx")
download_folder = "C:\\Users\\rafae\\Desktop\\PROGRAMAÇÃO\\PHYTON\\projeto"
kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}
x=10
time.sleep(1)
today = date.today()
hoje=today.strftime("%y.%m.%d")
final_url = driver.current_url
response = request.urlretrieve(final_url, "%sITIV %s.html"%(hoje,x))
save_webpage(final_url, download_folder)