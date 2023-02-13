#!/usr/bin/env python
# coding: utf-8




#Limpando dados da base

import pandas as pd
base = pd.read_excel(r'C:\Users\SAMSUNG\Desktop\base\ChavesClientes.xlsx')


base.head()

base.head()


#Verificando Cardinalidade desses dados


base.groupby(["Pagamento","ChaveSituacao"])["Pagamento"].count()


#começando a separar a string da coluna
text = '32FC'
text[2:3]


base['Idade'] = base.ChaveSituacao.str[:2]
base['genero'] = base.ChaveSituacao.str[2:3]
base['EstadoCivil'] = base.ChaveSituacao.str[-1]
base.head()


base.groupby(["Pagamento","EstadoCivil"])["Pagamento"].count()


display(base)



#Fazendo o split de um valor baseado em um delimitador
texto = 'Basic-Alpha'
texto.split('-')


base['Categoria'] = base.CatCliente.str.split('-').str.get(0)
base['CatVIP'] = base.CatCliente.str.split('-').str.get(1)
base.head()


#buscando a classificação do cliente dentro da coluna "Classe Risco"
import re


base['Risco'] = base.ClassRisco.apply(lambda x:re.findall('^[A-Z][^A-Za-z]?' , x)[0])
base.head()


#apresentando a tipagem da idade vemos que ela está como objeto e não número
base.info()

#fazendo com que a idade seja do tipo número
base['Idade'] = pd.to_numeric(base['Idade'])


base.info()


#Tratando valores vazios
base.loc[base.CatVIP.isnull(),"CatVIP"] = "Comum"
base.head()


#Finalizando limpeza deixando apenas as colunas organizadas
base.drop(["ChaveSituacao"], axis=1, inplace=True)
base.drop(["ClassRisco"], axis=1, inplace=True)
base.drop(["CatCliente"], axis=1, inplace=True)

display(base)

