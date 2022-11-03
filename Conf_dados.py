import json
import time
import numpy as np
import pandas as pd
import requests
import xlrd
from lib2to3.pgen2.driver import Driver
from webbrowser import Chrome
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#import webdriver
driver = webdriver.Chrome("C:\\Users\\rafae\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
# Acessa o site
driver.get('https://www.sefaz.salvador.ba.gov.br/IPTU/certidaoDadosCadastrais?Length=4#gsc.tab=0')
#Base de dados EXCEL
tabela = pd.read_excel("C:\\Users\\rafae\\Desktop\\PROGRAMAÇÃO\\PHYTON\\projeto\\DADOS.xlsx",dtype=object)
lin=tabela.shape[0]

#<img src="CaptchaImage.aspx?guid=b08bd352-0da1-4882-a1a9-bb4c6369ebfd" border="0" width="180" height="50">



#input    /html/body/form/div[3]/div/div[3]/div[1]/div[1]/input
#Digite o Nº da inscrição  e clique em 'Consultar'.    /html/body/form/div[3]/div/div[2]/h1
#Butão    /html/body/form/div[3]/div/div[3]/div[2]/input[2]
#Captcha da erro as vezes colocar um enter depois de clickar o botão e antes de pegar a informação
#Inscr mobiliaria /html/body/form/div[3]/div/div[2]/div[1]/table[1]/tbody/tr[1]/td[2]/span
#Proprietario /html/body/form/div[3]/div/div[2]/div[1]/table[1]/tbody/tr[2]/td[2]/span
#CPF /html/body/form/div[3]/div/div[2]/div[1]/table[1]/tbody/tr[3]/td[2]/span
time.sleep(5)