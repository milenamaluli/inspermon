#inspermon
def batalha():
	while vidaminha>0 and vidainimigo>0:
		vidainimigo=vidainimigo-(poderminha-defesainimigo)
		if vidainimigo<=0:
			return("Voce ganhou!")
		vidaminha=vidaminha-(poderinimigo-defesaminha)
		if vidaminha<=0:
			return("Voce perdeu...")
			