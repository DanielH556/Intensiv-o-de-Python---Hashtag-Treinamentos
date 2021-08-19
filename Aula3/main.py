from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from IPython.display import display

nav = webdriver.Edge(executable_path='C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe')

# Pesquisar cotação do dólar
nav.get('https://www.google.com/')
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cot_dolar = nav.find_element_by_xpath('/html/body/div[7]/div/div[8]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value') #data-value = variável que contém o valor da cotação
print(cot_dolar)

# Pesquisar cotação do euro
nav.get('https://www.google.com/')
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cot_euro = nav.find_element_by_xpath('/html/body/div[7]/div/div[8]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cot_euro)

# Pesquisar cotação do ouro
nav.get('https://www.melhorcambio.com/')
aba_original = nav.window_handles[0]
nav.find_element_by_xpath('/html/body/div[15]/div[2]/div/table[2]/tbody/tr[2]/td[2]/a/img').click()
aba_nova = nav.window_handles[1]
nav.switch_to.window(aba_nova)

cot_ouro = nav.find_element_by_id('comercial').get_attribute('value')
cot_ouro = cot_ouro.replace(',', '.')
print(cot_ouro)

# Planilha
produtos_df = pd.read_excel('C:\\Users\\User\\Desktop\\Estudos\\Intesivão de Python - Hashtag Treinamentos\\Aula3\\Produtos.xlsx')

produtos_df.loc[produtos_df['Moeda']=='Dólar', 'Cotação'] = float(cot_dolar)
produtos_df.loc[produtos_df['Moeda']=='Euro', 'Cotação'] = float(cot_euro)
produtos_df.loc[produtos_df['Moeda']=='Ouro', 'Cotação'] = float(cot_ouro)

produtos_df['Preço Base Reais'] = produtos_df['Cotação'] * produtos_df['Preço Base Original']
produtos_df['Preço Final'] = produtos_df['Margem'] * produtos_df['Preço Base Reais']

produtos_df.to_excel("Aula3/Produtos Atualizados.xlsx", index=False)
display(produtos_df)