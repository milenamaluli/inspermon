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
        a=batalha()
	if a==("Voce perdeu..."):
		break
	if a==("Voce ganhou"):
		continue
