import json
import random
with open('inspermons.json') as arquivo:
 	lista_inimigos = json.load(arquivo)

inimigo = random.choice(lista_inimigos)

vidainimigo=inimigo["vida"]
poderinimigo=inimigo["poder"]
defesainimigo=inimigo["defesa"]

print("Oi, eu sou o Miaredic. Eu tenho um poder de ataque de ataque de 20, uma vida de 250 e uma defesa de 10")

vidaminha=250
poderminha=20
defesaminha=10

insperdex=[]
vitorias =0

def sair():
	return 1
def ficar():
	return 2

def batalha(vidaminha, vidainimigo, poderminha,poderinimigo, defesainimigo, defesaminha,vitorias):
	inimigo = random.choice(lista_inimigos)

	vidainimigo=inimigo["vida"]
	poderinimigo=inimigo["poder"]
	defesainimigo=inimigo["defesa"]

	print(inimigo)
	while vidaminha>0 and vidainimigo>0:
		

		a=int(input("\n Opcao 1:batalhar 2:fugir"))

		if a==1:			

			vidainimigo=vidainimigo-(poderminha-defesainimigo)+ random.randint(-5,5)
			
			if vitorias>= 3:
				y = int(input ("parabens, voce ganhou um poder! 1 para usar,  2 para armazenar"))
				if y == 1:
					vidainimigo -= 10
					vitorias -= 3
					print ("POW! seu inimigo tomou uma surra!")
				else:
					print("voce tem um poder armazenado")

			if vidainimigo<=0:
				print("Voce ganhou!")
				return 3

			if vidainimigo==0:
				vidaminha+=100

			vidaminha=vidaminha-(poderinimigo-defesaminha)+ random.randint(-5,5)

			if vidaminha<=0:
				print("Voce perdeu...")
				return 1
			print("Vida do inimigo:")
			print(vidainimigo)
			print("Sua vida:")
			print(vidaminha)


		if a==2:
			d=random.choice([sair,ficar])()
			if d==1:
				print("Ocorreu um empate")
				return 2
				
			if d==2:
				print("Ixi! Nao vai dar para fugir dessa batalha!")
				continue
			


import random
while True :
	
	print("\n opcoes \n 1: passear opcao \n 2: dormir \n 3:ver insperdex \n " )
	opcao  = int(input("escolha uma opcao: "))    
	if opcao == 2:
		break
	if opcao == 1 :
		a=batalha(vidaminha, vidainimigo, poderminha,poderinimigo, defesainimigo, defesaminha,vitorias)
		print(a)

		if a==1:
			inimigo["vida"]+=5
						
			continue
		if a==2:
			continue

		if a==3:
			print("in")
			insperdex.append(inimigo)
			inimigo["vida"]-=5
			vitorias+=1
			continue
			
		
	if opcao==3:
		print(insperdex)

	
	with open('inspermons.json', 'w') as arquivo:
		json.dump(lista_inimigos,arquivo)

	with open('vitorias.json', 'w') as arquivo:
		json.dump(vitorias,arquivo)

	with open('insperdex.json', 'w') as arquivo:
		json.dump(insperdex,arquivo)

