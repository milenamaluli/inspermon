#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:11:40 2017

@author: arihalpern
"""
import random
while True :
    print("opcao 1: passear opcao 2: dormir")
    opcao  = int(input("escolha uma opcao"))    
    if opcao == 2:
        break
    if opcao == 1 :
        inimigo = random.choice(lista_inimigos)
        print(inimigo)
        #inspermon
def batalha():
	while vidaminha>0 and vidainimigo>0:
		vidainimigo=vidainimigo-(poderminha-defesainimigo)
		if vidainimigo<=0:
			return("Voce ganhou!")
		vidaminha=vidaminha-(poderinimigo-defesaminha)
		if vidaminha<=0:
			return("Voce perdeu...")