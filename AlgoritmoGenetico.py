from Cromossomo import Cromossomo
import random
from operator import attrgetter

class AlgoritmoGenetico:

		
	def __init__(self,nrGenes,tamanhoPopulacao):
		self.tamanhoPopulacao = tamanhoPopulacao
		self.populacao = self.criaPopulacaoInicial(nrGenes)
		self.pesos=[1,2,3,4,5,6,7,8,9,10]
		self.valores=[10,20,30,40,50,60,70,80,90,100]
		self.pesoMaximo=70
		self.probabilidadeCruzamento=70
		self.probabilidadeMutacao=5

	def cruzamentoUmPonto(self,cromo1,cromo2):
		numGenes = len(cromo1.genes)
		pontoCorte = random.randrange(numGenes)
		genes1 = cromo1.genes[0:pontoCorte] + cromo2.genes[pontoCorte:numGenes]
		genes2 = cromo2.genes[0:pontoCorte] + cromo1.genes[pontoCorte:numGenes]
		filho1 = Cromossomo(5)
		filho2 = Cromossomo(5)
		filho1.genes = genes1
		filho2.genes = genes2
		return filho1,filho2


	def mutacao(self,cromossomo):
		for i in range(0,len(cromossomo.genes)):
			prob = random.randrange(100)
			if(prob < self.probabilidadeMutacao):
				if cromossomo.genes[i]==1:
					cromossomo.genes[i]=0
				else:
					cromossomo.genes[i]=1


	def calculaFitness(self):
		for cromossomo in self.populacao:
			pesoTotal=0
			valorTotal=0
			for i in range(0,len(cromossomo.genes)):
				if(cromossomo.genes[i]==1):
					pesoTotal += self.pesos[i]
					valorTotal += self.valores[i]
			if(pesoTotal > self.pesoMaximo):
				cromossomo.setFitness(0)
			else:
				cromossomo.setFitness(valorTotal)


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
			self.populacao.append(f1)
			self.populacao.append(f2)


	def seleciona(self):
		self.calculaFitness()
		novaPopulacao=[]
		best = self.getMelhorIndividuo()					# 
		novaPopulacao.append(best)							# elitismo
		for i in range(self.tamanhoPopulacao):
			c1 = random.randrange(len(self.populacao))
			c2 = random.randrange(len(self.populacao))
			cromossomoVencedor = self.torneio(self.populacao[c1],self.populacao[c2])
			if cromossomoVencedor not in novaPopulacao:
				novaPopulacao.append(cromossomoVencedor)
		self.populacao = novaPopulacao


	def torneio(self,cromossomo1,cromossomo2):
		if(cromossomo1.getFitness > cromossomo2.getFitness):
			return cromossomo1
		else:
			return cromossomo2

	def muta(self):
		best = self.getMelhorIndividuo()
		for cromossomo in self.populacao:
			if(id(best)!=id(cromossomo)): #nao executa mutacao no melhor individuo
				self.mutacao(cromossomo)

	
	def imprimePopulacao(self):
		print len(self.populacao)
		for cromossomo in self.populacao:
			print cromossomo.toString() + " " + self.getConfiguracaoMochila(cromossomo)

	def getConfiguracaoMochila(self,cromossomo):
		pesoTotal = 0
		valorTotal = 0
		for i in range(0,len(cromossomo.genes)):
			if(cromossomo.genes[i]==1):
				pesoTotal += self.pesos[i]
				valorTotal += self.valores[i]
		return "peso: {0}, valor: {1}".format(pesoTotal,valorTotal)

	def getMelhorIndividuo(self):
		return max(self.populacao, key=attrgetter('fitness'))



