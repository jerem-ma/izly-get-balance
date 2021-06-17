#!/bin/python
import requests as rq
import re

# Get credentials
# They have to be username\npassword
login = passw = None
with open('izly_credentials', 'r') as file:
    credentials = file.read()
    login, passw = re.search('(.*)\n(.*)\n', credentials).groups()

# Connection
login = {'username': login, 'password': passw, 'returnUrl': ''}
r = rq.post("https://mon-espace.izly.fr/Home/Logon", data=login)

# Getting balance
balance = re.search('(\d+\.\d+)<em>\s€', r.text).groups()[0]

print("My balance is", balance + "€")
