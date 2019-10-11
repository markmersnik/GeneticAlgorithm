import random
import string 
import math
#Contains all of the functions required for the algorithm
class DNA:

	#Constructs our DNA object
	def __init__(self):
		self.genes = []
		self.fitnessScore = 0.0

		for i in range(0, 7):
			self.genes.append(random.choice(string.ascii_lowercase + " "))

	#Calculates the fitness based on number of letters that match
	def fitness(self):
		score = 0

		for i in range(0, len(self.genes)):
			if(self.genes[i] == Setup().target[i]):
				score += 1

		self.fitnessScore = score/len(Setup().target)
		self.fitnessScore = self.fitnessScore**2

	#Produces crossover between child and parent DNA
	def mate(self, parent):
		child = DNA()
		midpoint = random.randint(0, len(self.genes)-1)

		for i in range(0, len(self.genes)):
			if(i > midpoint):
				child.genes[i] = self.genes[i]
			else:
				child.genes[i] = parent.genes[i]
		return child

	#Adjusts the genes at the mutation rate
	def mutate(self):
		for i in range(0, len(self.genes)):
			if(round(random.uniform(0,1), 2) < Setup().mutationRate):
				self.genes[i] = random.choice(string.ascii_letters + " ")

	#Returns the genes list as a string.
	def checkString(self):
		phrase = ""
		for i in self.genes:
			phrase += i
		return phrase

#Creates the problem that utilizes our DNA functions
class Setup:

	#Sets up the attributes of our problem
	def __init__(self):
		self.mutationRate 		= 0.02
		self.totalPopulation 	= 100
		self.population 		= []
		self.matingPool 		= []
		self.target 			= "carrots"
		self.targetLength 		= len(self.target)
		self.targetHit 			= ""
		self.complete 			= False
		self.generations 		= 0
		self.numIterated		= self.totalPopulation

		for i in range(0, self.totalPopulation):
			self.population.append(DNA())

	#Calculates the average fitness of the current population
	def averagefit(self, num):
		return int(num/self.numIterated)

	#Performs the evolution of our problem
	def create(self):
		
		self.generations += 1

		avgFitness = 0
		topFitness = 0
		topPhrase = ""

		#Natural selection process
		for i in range(0, len(self.population)):
			self.population[i].fitness()
			print(self.population[i].checkString() + " --> ", end="")

		#Mating pool algorithm
		for i in range(0, self.totalPopulation):
			n = int(self.population[i].fitnessScore * 100)
			current_phrase = self.population[i].checkString()

			if(n > topFitness):
				topFitness = n
				topPhrase = self.population[i].checkString()
			avgFitness += int(((n/100)**.5)*100)

			if(current_phrase == self.target):
				self.complete = True
				self.numIterated = i
				break

			for j in range(0, n):
				self.matingPool.append(self.population[i])

		#Reproduction process
		for i in range(0, len(self.population)):
			if(self.complete):
				break

			matingPoolLength = len(self.matingPool)
			if(matingPoolLength > 0):
				a = random.randint(0, matingPoolLength - 1)
				b = random.randint(0, matingPoolLength - 1)

				partnerA = self.matingPool[a]
				partnerB = self.matingPool[b]
				
				child = partnerA.mate(partnerB)
				child.mutate()
				self.population[i] = child

		print("\n\nGeneration " + str(self.generations))
		print("Best Phrase: " + topPhrase)
		print("Avg Fitness " + str(self.averagefit(avgFitness)) + "\n\n")



#Runs the program.
d = Setup()
found = False

while(found == False):
	d.create()
	found = d.complete

print("Done!\n" + "Number of Generations: " + str(d.generations))
