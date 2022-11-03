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
driver.get("https://www.sefaz.salvador.ba.gov.br/Iptu/VUPC?Length=4#gsc.tab=0")
#Base de dados EXCEL
tabela = pd.read_excel("C:\\Users\\rafae\\Desktop\\PROGRAMAÇÃO\\PHYTON\\projeto\\DADOS.xlsx",dtype=object)
lin=tabela.shape[0]
#Mudando para o iframe
iframe = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/iframe")
driver.switch_to.frame(iframe)
resultado_dig=[]

for a in range (lin):
    #Pega a inscrição
    valor_inc=tabela.iloc[a]['INSCRIÇÃO']
    # Procura caixa de texto
    element = driver.find_element(By.XPATH, '/html/body/div[3]/form/input[1]')
    # Insere o dado
    element.send_keys(valor_inc)
    # Clicka em submit
    driver.find_element(By.XPATH, '/html/body/div[3]/form/p/input[1]').click()
    time.sleep(1)
    #Pegando comdando da pagina que diferencia entre resultado ("Resultado da Consulta") ou falha ("Digite a inscrição imobiliária")
    texto = driver.find_element(By.XPATH, '/html/body/div[2]/h1').text
    if (texto=="Resultado da Consulta"):
        encontrado = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div/table/tbody/tr[3]/td[1]').text
        #adicionar resultado ao excel
        resultado_dig.append(encontrado)
        driver.refresh()
        time.sleep(1)
        iframe = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/iframe")
        # switch to selected iframe
        driver.switch_to.frame(iframe)
    else:
        resultado_dig.append("Não encontrado.")
    print(resultado_dig)

tabela["RESULTADO"] = resultado_dig
tabela.to_excel("C:\\Users\\rafae\\Desktop\\PROGRAMAÇÃO\\PHYTON\\projeto\\DADOSPANDAS.xlsx")
time.sleep(5)

    



