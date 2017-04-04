import json
import random
with open('inspermons.json') as arquivo:
 	lista_inimigos = json.load(arquivo)


inimigo = random.choice(lista_inimigos)
print(inimigo["nome"])


print("Oi, eu sou o Miaredic. Eu tenho um poder de ataque de ataque de 20, uma vida de 250 e uma defesa de 10")

vidaminha=250
poderminha=20
defesaminha=10

vidainimigo=inimigo["vida"]
poderinimigo=inimigo["poder"]
defesainimigo=inimigo["defesa"]


def batalha(vidaminha, vidainimigo, poderminha,poderinimigo, defesainimigo, defesaminha):
	while vidaminha>0 and vidainimigo>0:
		a=int(input("\n Opcao 1:batalhar 2:fugir"))
		if a==1:

			vidainimigo=vidainimigo-(poderminha-defesainimigo)
			if vidainimigo<=0:
				print("Voce ganhou!")
			if vidainimigo==0:
				vidaminha+=100
			vidaminha=vidaminha-(poderinimigo-defesaminha)
			if vidaminha<=0:
				print("Voce perdeu...")
			print(vidainimigo)
			print(vidaminha)


		if a==2:
			#adicionar probabilidade de fuga
			print("Ocorreu um empate")



insperdex=[]		
import random
while True :

	print("\n opcao 1: passear opcao \n 2: dormir \n 3:ver insperdex" )
	opcao  = int(input("escolha uma opcao"))    
	if opcao == 2:
		break
	if opcao == 1 :
		print(inimigo)
		a=batalha(vidaminha, vidainimigo, poderminha,poderinimigo, defesainimigo, defesaminha)
		print(a)
		if a==("Voce perdeu...") or a==("Ocorreu um empate"):
			break
		if a==("Voce ganhou"):
			insperdex.append(inimigo)
			continue
		if opcao==3:
			print(insperdex)

