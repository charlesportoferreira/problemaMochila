from AlgoritmoGenetico import AlgoritmoGenetico


if __name__ == '__main__':

	ag = AlgoritmoGenetico(10,10)
	print "***********  populacao inicial ***************"
	ag.imprimePopulacao()

	ag.calculaFitness()

	for i in range(100):
		print "\n\n************************  Geracao: {0}".format(i) 
		ag.cruza()	
		ag.muta()
		ag.seleciona()
		# ag.imprimePopulacao()
		best = ag.getMelhorIndividuo()
		print "\nMelhor individuo-> {0} \n".format(ag.getConfiguracaoMochila(best))
	