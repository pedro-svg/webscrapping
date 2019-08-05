# -*- coding: utf-8 -*-
# coding: UTF-8
import requests
from bs4 import BeautifulSoup
from csv import writer 

url = 'https://bocadoinferno.com.br/criticas/'

response = requests.get(url)

# Código 200 talkey
print(f'Estado da requisição: {response.status_code}')

# Retorna um dicionário, com as informações não visíveis da página
print(response.headers)

#Salva o document da página
src = response.content

soup = BeautifulSoup(src,'lxml')
soup.prettify()
title_list = soup.find_all('h2',  class_='entry-title')

for titlex in title_list:
  print(titlex.a.attrs['title'])
  
#Usando o método select 
#devolve um array de elementos

with open('title.csv','w') as csv_file:
  csv_writer = writer(csv_file)
  header = ['Lista de Filmes']
  csv_writer.writerow(header)

  for text in soup.select('.tptn_title'):
    title = text.get_text() 
    csv_writer.writerow([title])

