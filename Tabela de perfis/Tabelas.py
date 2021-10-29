# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:10:20 2021

@author: João Gomes
"""


import pandas as pd
import numpy as np


def dadosPerfil(tipo):
    perfis = pd.read_excel('Perfis.xlsx')
    perfil = perfis.loc[perfis[0] == tipo]
    ind = perfil.shape[1]
    
    
    
    dados = np.zeros((ind - 1,1))
    for i in range (1, ind):
        dados[i-1,0] = perfil[i]
            
    dados = dados[dados != 0]
    
    
    entrada = pd.read_excel('tipo.xlsx')
    titulos = entrada.loc[entrada['Código'] == dados[-1]]
    loc = int(titulos['index'])
    titulos = entrada.loc[entrada['Código'] == dados[-1]].loc[loc]
    titulos.pop('index')
    titulos.pop('perfil')
    titulos.pop('Código')
    titulos = titulos[titulos != 0]
    dados = np.delete(dados, -1, 0)
    final = {}
    for i in range (dados.shape[0]):
        final[titulos[i]] = dados[i]
    return final
