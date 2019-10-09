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
		print(round(random.uniform(0,1), 2))

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

	def mutate():
		for i in range(0, len(self.genes)):
			if(round(random.uniform(0,1), 2) < Setup().mutationRate):
				self.genes[i] = random.choice(string.ascii_letters + " ")

class Setup:

	def __init__(self):
		self.mutationRate = 0.01
		self.totalPopulation = 150
		self.population = []
		self.matingPool = []
		self.target = "to be or not to be"

	def create(self):
		for i in range(0, len(self.population)):
			self.population[i].fitness

		for i in range(0, self.totalPopulation):
			self.population.append(DNA())

		for i in range(0, self.totalPopulation):
			n = int(self.population[i].fitnessScore * 100)

			for j in range(0, n):
				self.matingPool.append(self.population[i])

		#Reproduction
		for i in range(0, len(self.population)):
			matingPoolLength = len(self.matingPool)

			if(matingPoolLength > 0):
				a, b = random.randint(0, matingPoolLength - 1)
			
				partnerA = self.matingPool[a]
				partnerB = self.matingPool[b]
				
				child = partnerA.mate(partnerB)
				child.mutate()

				self.population[i] = child



d = Setup()
while(True):
	d.create()
