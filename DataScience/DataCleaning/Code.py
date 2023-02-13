#!/usr/bin/env python
# coding: utf-8

# In[388]:


#Limpando dados da base


# In[389]:


import pandas as pd
base = pd.read_excel(r'C:\Users\SAMSUNG\Desktop\base\ChavesClientes.xlsx')


# In[390]:


base.head()


# In[391]:


base.head()


# In[392]:


#Verificando Cardinalidade desses dados


# In[393]:


base.groupby(["Pagamento","ChaveSituacao"])["Pagamento"].count()


# In[394]:


#começando a separar a string da coluna
text = '32FC'
text[2:3]


# In[395]:


base['Idade'] = base.ChaveSituacao.str[:2]
base['genero'] = base.ChaveSituacao.str[2:3]
base['EstadoCivil'] = base.ChaveSituacao.str[-1]
base.head()


# In[396]:


base.groupby(["Pagamento","EstadoCivil"])["Pagamento"].count()


# In[397]:


display(base)


# In[ ]:





# In[398]:


#Fazendo o split de um valor baseado em um delimitador
texto = 'Basic-Alpha'
texto.split('-')


# In[399]:


base['Categoria'] = base.CatCliente.str.split('-').str.get(0)
base['CatVIP'] = base.CatCliente.str.split('-').str.get(1)
base.head()


# In[400]:


#buscando a classificação do cliente dentro da coluna "Classe Risco"
import re


# In[401]:


base['Risco'] = base.ClassRisco.apply(lambda x:re.findall('^[A-Z][^A-Za-z]?' , x)[0])
base.head()


# In[402]:


#apresentando a tipagem da idade vemos que ela está como objeto e não número
base.info()


# In[403]:


#fazendo com que a idade seja do tipo número
base['Idade'] = pd.to_numeric(base['Idade'])


# In[404]:


base.info()


# In[405]:


#Tratando valores vazios
base.loc[base.CatVIP.isnull(),"CatVIP"] = "Comum"
base.head()


# In[406]:


#Finalizando limpeza deixando apenas as colunas organizadas
base.drop(["ChaveSituacao"], axis=1, inplace=True)
base.drop(["ClassRisco"], axis=1, inplace=True)
base.drop(["CatCliente"], axis=1, inplace=True)

display(base)

