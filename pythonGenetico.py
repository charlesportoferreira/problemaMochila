from pyevolve import G2DList
from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Crossovers
from pyevolve import Mutators
# from sklearn import datasets
import pyevolve
import math

objetivo=25;
pesos=[1,2,5,10,3,4]

def eval_func(chromosome):
    fitness = 0;
    for i in range(0,len(chromosome)):
    	fitness += pesos[i]
    
    return fitness

# pyevolve.logEnable()
genome = G1DList.G1DList(6)
genome.setParams(rangemin=0, rangemax=1,bestRawScore=15)

genome.evaluator.set(eval_func)
# genome.crossover.set(Crossovers.G2DListCrossoverSingleHPoint)
# genome.mutator.set(Mutators.G2DListMutatorIntegerGaussian)

ga = GSimpleGA.GSimpleGA(genome)
ga.selector.set(Selectors.GRouletteWheel)
ga.setGenerations(100)

pop = ga.getPopulation()
pop.setPopulationSize(5)

ga.evolve(freq_stats=1)



print ga.getPopulation()


# Best individual
best = ga.bestIndividual()
print "\nBest individual score: %.2f" % (best.score,)
# print best
