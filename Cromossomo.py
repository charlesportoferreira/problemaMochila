import random

class Cromossomo:

	def __init__(self,nrGenes):
		self.fitness = 0
		self.genes = []
		self.nrGenes = nrGenes
		self.inicializa()

	def inicializa(self):
		for i in range(0,self.nrGenes):
			self.genes.append(random.randrange(2))

	def setFitness(self,valor):
		self.fitness = valor

	def getFitness(self):
		return self.fitness

	def toString(self):
		return "genes {0}, fitness {1}, id {2}".format(self.genes,self.fitness,id(self))

