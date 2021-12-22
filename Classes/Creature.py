import Genome

dirs = {
	0: [0, -1],
	1: [1, -1],
	2: [1, 0],
	3: [1, 1],
	4: [0, 1],
	5: [-1, 1],
	6: [-1, 0],
	7: [-1, -1]
}

class Creature():

	c_pos = [0,0]
	dir_faced = 0
	next_cell = dirs[dir_faced]

	def __init__(self, parent_genome, window_offsets, mut_mod):
		self.parent_genome = parent_genome
		self.mut_mod = mut_mod
		self.c_pos[0] = c_pos[0] + window_offsets[0] + window_offsets[2]
		self.c_pos[1] = c_pos[1] + window_offsets[1] + window_offsets[3]
		self.genome = Genome(mut_mod, parent_genome)
		self.brain = Brain(self.genome.get_genes())

	def get_genome():
		return self.genome

	def get_brain():
		return self.brain

	def get_pos():
		return c_pos

	def get_dir():
		return dir_faced

	def get_next_cell():
		output = [0,0]
		output[0] = c_pos[0] + next_cell[0]
		output[1] = c_pos[1] + next_cell[1]
		return output