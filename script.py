# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# coding: UTF-8

url = 'https://bocadoinferno.com.br/criticas/'
request = requests.get(url)

# Código 200 talkey
  # print(request.status_code)

# Retorna um dicionário, com as informações não visíveis da página
  # print(request.headers)

# Guarda o document da página
src = request.content

soup = BeautifulSoup(src,'lxml')
soup.prettify()
title_list = soup.find_all('h2',  class_='entry-title')


for titlex in title_list:
  print(titlex.a.attrs['title'])