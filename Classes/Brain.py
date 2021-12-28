import random

class Brain():

	nodes = []

	def __init__(self, genome):
		self.genome = genome
		wire_brain()

	def wire_brain():
		return
	def get_creature_data(creature):
		self.c_age = creature.get_age()


	def on_step():
		for x in nodes:
			trigger = random.randint(0, 255)
			if nodes[x].get_sensitivity() < trigger:
				return
				