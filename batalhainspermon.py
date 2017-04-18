import json
with open('inspermons.json') as arquivo:
 	lista_inimigos = json.load(arquivo)

print(lista_inimigos[inimigo]["nome"])

print("Oi, eu sou o Miaredic. Eu tenho um poder de ataque de ataque de 20, uma vida de 250 e uma defesa de 10")

vidaminha=250
poderinha=20
defesaminha=10

vidainimigo=lista_inimigos[inimigo]["vida"]
poderinimigo=lista_inimigos[inimigo]["poder"]
defesainimigo=lista_inimigos[inimigo]["defesa"]

def batalha():
	while vidaminha>0 and vidainimigo>0:
		vidainimigo=vidainimigo-(poderminha-defesainimigo)
		if vidainimigo<=0:
			return("Voce ganhou!")
		vidaminha=vidaminha-(poderinimigo-defesaminha)
		if vidaminha<=0:
			return("Voce perdeu...")
		
			