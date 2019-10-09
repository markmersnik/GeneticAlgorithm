import random
import string 
from setup import *

class DNA:

	def __init__(self):

		self.genes = []
		self.fitness

		for i in range(0, 18):
			genes.append(random.choice(string.ascii_letters)) 


	def fitness():
		int score = 0
		for i in range(0, len(genes)):
			if(genes[i] == Setup.self.target[i]):
				score += 1
		self.fitness = score/len(Setup.self.target)


	def mutate(mutationRate):
		


