from Cromossomo import Cromossomo
import random

class AlgoritmoGenetico:

		
	def __init__(self,nrGenes,tamanhoPopulacao):
		self.tamanhoPopulacao = tamanhoPopulacao
		self.populacao = self.criaPopulacaoInicial(nrGenes)
		self.pesos=[1,2,3,4,5]
		self.valores=[10,20,30,40,50]
		self.probabilidadeCruzamento=70
		self.probabilidadeMutacao=0.01

	def cruzamentoUmPonto(self,cromo1,cromo2):
		genes1 = cromo1.genes[0:2] + cromo2.genes[2:5]
		genes2 = cromo2.genes[0:2] + cromo1.genes[2:5]
		filho1 = Cromossomo(5)
		filho2 = Cromossomo(5)
		filho1.genes = genes1
		filho2.genes = genes2
		return filho1,filho2


	def mutacao(self,cromossomo):
		print "executando mutacao"
		pos = random.randrange(len(cromossomo.genes))
		print pos
		cromossomo.genes[pos] = random.randrange(2)


	def calculaFitness(self):
		for cromossomo in self.populacao:
			pesoTotal=0
			valorTotal=0
			for i in range(0,len(cromossomo.genes)):
				if(cromossomo.genes[i]==1):
					pesoTotal += self.pesos[i]
					valorTotal += self.valores[i]
			cromossomo.setFitness(valorTotal)
			self.populacao.sort(key=lambda x: x.fitness, reverse=True)
			# print "peso {0}, valor {1}".format(pesoTotal, valorTotal)

	def criaPopulacaoInicial(self,nrGenes):
		populacao = []
		for i in range(0,self.tamanhoPopulacao):
			cromo = Cromossomo(nrGenes)
			populacao.append(cromo)
		return populacao

	def cruza(self):
		cromossomos=[]
		for cromossomo in self.populacao:
			prob = random.randrange(100)
			if(prob <= self.probabilidadeCruzamento):
				cromossomos.append(cromossomo)
		for x in range(0,len(cromossomos),2):
			if (x+1 >= len(cromossomos)):
				break
			f1,f2 = self.cruzamentoUmPonto(cromossomos[x],cromossomos[x+1])
			print "teste cruzamento {0}, {1}".format(cromossomos[x].fitness, cromossomos[x+1].fitness)
			self.populacao.append(f1)
			self.populacao.append(f2)

	def seleciona(self):
		novaPopulacao=[]
		novaPopulacao.append(self.populacao[0])#elitismo
		for i in range(self.tamanhoPopulacao):
			c1 = random.randrange(len(self.populacao))
			c2 = random.randrange(len(self.populacao))
			print "i,c1,c2: {0}, {1}, {2}".format(i,self.populacao[c1].fitness,self.populacao[c2].fitness)
			cromossomoVencedor = self.torneio(self.populacao[c1],self.populacao[c2])
			if cromossomoVencedor not in novaPopulacao:
				novaPopulacao.append(cromossomoVencedor)
			# novaPopulacao.append(self.torneio(self.populacao[c1],self.populacao[c2]))
		self.populacao = novaPopulacao
		self.populacao.sort(key=lambda x: x.fitness, reverse=True)


	def torneio(self,cromossomo1,cromossomo2):
		if(cromossomo1.getFitness > cromossomo2.getFitness):
			return cromossomo1
		else:
			return cromossomo2



x = AlgoritmoGenetico(5,10)
a = x.populacao
print "***********  populacao inicial ***************"
for cromossomo in a:
	print cromossomo.toString()



x.calculaFitness()

for i in range(100):
	print "\n\n************************  Geracao: {0}".format(i) 
	print "**  apos cruzamento **"
	x.cruza()	
	x.calculaFitness()
	for cromossomo in a:
		print cromossomo.toString()
	
	print "\n\n**  apos selecao **"
	x.seleciona()
	a = x.populacao
	for cromossomo in a:
		print cromossomo.toString()
# filho1,filho2 = x.cruzamento(x.pop[0],x.pop[1])

# print filho1.genes
# print filho2.genes

# print len(x.pop[0].genes)

# x.mutacao(x.pop[0])

# print x.pop[0].genes



# for cromossomo in a:
# 	print cromossomo.getFitness()
# x = AlgoritmoGenetico()
# x.cruzamento()
# x.mutacao()
# x.getFitness()

# b = []

# for i in range(0,30):
# 	c = Cromossomo(5)
# 	b.append(c)


# for p in b:
# 	print p.genes