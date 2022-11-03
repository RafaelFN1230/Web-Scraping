import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

#import webdriver
driver = webdriver.Chrome("C:\\Users\\rafae\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe")
# Acessa o site
driver.get("https://dti.sefaz.salvador.ba.gov.br/Modulos/DTI/ItivDeclaracaoFrm.aspx")
#Base de dados EXCEL
tabela = pd.read_excel("C:\\Users\\rafae\\Desktop\\PROGRAMAÇÃO\\PHYTON\\projeto\\DADOS.xlsx",dtype=object)
lin=tabela.shape[0]
resultado_dig=[]
def caixa_escolha():
    # Clicka em caixa de escolha
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[2]/select').click()
    time.sleep(1)
    # Escolhe "Inscrição imobiliaria"
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[2]/select/option[2]').click()
    time.sleep(1)
caixa_escolha()
for a in range (lin):
   
    #Pega a inscrição
    valor_inc=tabela.iloc[a]['INSCRIÇÃO']
    valor_dig=tabela.iloc[a]['DIGITO']
    incs_compl=str(valor_inc)+"-"+str(valor_dig)
    # Procura caixa de texto da inscrição
    element = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[5]/input[1]')
    # Insere o dado
    element.send_keys(valor_inc)
    # Procura caixa de texto do digito
    element = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[5]/input[2]')
    # Insere o dado
    element.send_keys(valor_dig)
    time.sleep(5)
    #Salvando o resultado
     #Clicka em consulta
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/table/tbody/tr[2]/td/div/input').click()
    #Espera o Usuario inserir o captcha
    time.sleep (15)
    driver.refresh()
    caixa_escolha()
