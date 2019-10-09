import random
import string 

class DNA :


	def __init__(self):

		self.genes = []
		self.fitnessScore = 0.0

		for i in range(0, 18):
			self.genes.append(random.choice(string.ascii_letters + " "))
			print(self.genes[i], end="")
		print("")


	def fitness(self):
		score = 0
		for i in range(0, len(self.genes)):
			if(self.genes[i] == Setup().target[i]):
				score += 1
		self.fitnessScore = score/len(Setup().target)
		print(self.fitnessScore)

	#crossover between child and parent DNA
	def mate(parent):
		child = DNA()
		midpoint = random.randint(0, len(self.genes)-1)
		for i in range(0, len(self.genes)):
			if(i > midpoint):
				child.genes[i] = self.genes[i]
			else:
				child.genes[i] = parent.genes[i]
		return child

	#def mutate(mutationRate):


	def currentPopulation(self):
		for i in self.genes:
			print(i)

class Setup:

	def __init__(self):
		self.mutationRate = 0.01
		self.totalPopulation = 150
		self.population = []
		self.matingPool = []
		self.target = "to be or not to be"

		for i in range(0, self.totalPopulation):
			self.population.append(DNA())


	#def create():

d = DNA()
d.fitness()
