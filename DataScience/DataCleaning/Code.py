#!/usr/bin/env python
# coding: utf-8




#Cleaning the data base

import pandas as pd
base = pd.read_excel(r'C:\Users\SAMSUNG\Desktop\base\ChavesClientes.xlsx')


base.head()

base.head()


#Checking the cardinality of this data


base.groupby(["Pagamento","ChaveSituacao"])["Pagamento"].count()


#starting to separate string from column
text = '32FC'
text[2:3]


base['Idade'] = base.ChaveSituacao.str[:2]
base['genero'] = base.ChaveSituacao.str[2:3]
base['EstadoCivil'] = base.ChaveSituacao.str[-1]
base.head()


base.groupby(["Pagamento","EstadoCivil"])["Pagamento"].count()


display(base)



#Splitting a value based on a delimiter
texto = 'Basic-Alpha'
texto.split('-')


base['Categoria'] = base.CatCliente.str.split('-').str.get(0)
base['CatVIP'] = base.CatCliente.str.split('-').str.get(1)
base.head()


#searching for the client's classification within the "Classe Risco" column
import re


base['Risco'] = base.ClassRisco.apply(lambda x:re.findall('^[A-Z][^A-Za-z]?' , x)[0])
base.head()


#presenting the age typing we see that it is as an object and not a number
base.info()

#making the age type number
base['Idade'] = pd.to_numeric(base['Idade'])


base.info()


#Handling empty values
base.loc[base.CatVIP.isnull(),"CatVIP"] = "Comum"
base.head()


#Finishing cleaning leaving only the columns organized
base.drop(["ChaveSituacao"], axis=1, inplace=True)
base.drop(["ClassRisco"], axis=1, inplace=True)
base.drop(["CatCliente"], axis=1, inplace=True)

display(base)

