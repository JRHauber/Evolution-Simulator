import random

class Brain():

	nodes = []

	def __init__(self, genome):
		self.genome = genome
		wire_brain()

	def wire_brain():

	def on_step():
		for x in nodes:
			trigger = random.randint(0, 255)
			if nodes[x].get_sensitivity() < trigger:
				