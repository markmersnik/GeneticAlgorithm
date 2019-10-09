import random
import string 


class DNA :

	#Constructs our 
	def __init__(self):
		self.genes = []
		self.fitnessScore = 0.0
		for i in range(0, 2):
			self.genes.append(random.choice(string.ascii_letters + " "))


	def fitness(self):
		score = 0
		for i in range(0, len(self.genes)):
			if(self.genes[i] == Setup().target[i]):
				score += 1
		self.fitnessScore = score/len(Setup().target)

	#Crossover between child and parent DNA
	def mate(self, parent):
		child = DNA()
		midpoint = random.randint(0, len(self.genes)-1)
		for i in range(0, len(self.genes)):
			if(i > midpoint):
				child.genes[i] = self.genes[i]
			else:
				child.genes[i] = parent.genes[i]
		return child

	def mutate(self):
		for i in range(0, len(self.genes)):
			if(round(random.uniform(0,1), 2) < Setup().mutationRate):
				self.genes[i] = random.choice(string.ascii_letters + " ")

	def checkString(self):
		phrase = ""
		for i in self.genes:
			phrase += i

		return phrase

class Setup:

	def __init__(self):
		self.mutationRate = 0.05
		self.totalPopulation = 500
		self.population = []
		self.matingPool = []
		self.target = "to"
		self.targetHit = ""
		self.complete = False
		self.count = 1

		for i in range(0, self.totalPopulation):
			self.population.append(DNA())

	def create(self):
		
		#This is where CheckPop() was.
		if(self.complete == False):
			for i in range(0, self.totalPopulation):
				#print(str(self.count) + ") ", end="")
				phrase = self.population[i].checkString()
				#print(phrase)
				self.isCompleted(phrase)
				self.count += 1
				n = int(self.population[i].fitnessScore * 100)

				for j in range(0, n):
					self.matingPool.append(self.population[i])

			#Reproduction
			for i in range(0, len(self.population)):
				matingPoolLength = len(self.matingPool)

				if(matingPoolLength > 0):
					a = random.randint(0, matingPoolLength - 1)
					b = random.randint(0, matingPoolLength - 1)

					partnerA = self.matingPool[a]
					partnerB = self.matingPool[b]
					
					child = partnerA.mate(partnerB)
					child.mutate()

					self.population[i] = child
		else:
			print("Done")


	def checkPop():
		for i in range(0, len(self.population)):
			self.population[i].fitness()
			self.targetHit = self.population[i].checkString()
			self.isCompleted(self.targetHit)
			#print(self.population[i].fitnessScore)

	def isCompleted(self, phrase):
		if(phrase is self.target):
			self.complete = True




d = Setup()
while(d.complete == False):
	print(str(d.count + d.complete))
	d.create()
