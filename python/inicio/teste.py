#!/usr/bin/python2.7

import requests
from requests.auth import HTTPBasicAuth

#dados de autenticacao

URL_ACESSO = "http://visitante.acesso.uol.com.br/login.html"
USER = "rabuchaim"
PASSWD = "jul1nh4U0L"

#Consulta a URL de acesso 
res = requests.post(URL_ACESSO, verify=False, auth=HTTPBasicAuth(USER, PASSWD)

if res.status_code == 200:
    break
 