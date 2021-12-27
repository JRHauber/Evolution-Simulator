class Node():

	designations = {
		0: 'Pheromone Gradient X',
		1: 'Pheromone Gradient Fw',
		2: 'Pheromone Density',
		3: 'Age',
		4: 'RND',
		5: 'Blockage X',
		6: 'Oscillator',
		7: 'Blockage Fw',
		8: 'Population Gradient X',
		9: 'Population Density',
		10: 'Population Gradient Fw',
		11: 'Long-Range Population Fw',
		12: 'Last Movement Y',
		13: 'Long-Range Blockage Fw',
		14: 'Last Movement X',
		15: 'Y Border Distance',
		16: 'Genetic Similarity Fw',
		17: 'X Border Distance',
		18: 'X Position',
		19: 'Nearest Border Distance',
		20: 'Y Position',
		21: 'Internal Neuron',
		22: 'Set Long-Range Distance',
		23: 'Kill Forward Neighbor',
		24: 'Set Oscillator Period',
		25: 'Emit Pheromone',
		26: 'Set Responsiveness',
		27: 'Move Forward',
		28: 'Move Random',
		29: 'Move Reverse',
		30: 'Move Left-Right',
		31: 'Move X',
		32: 'Move Y'
	}



	def __init__(self, intensity_gene, connect_gene, designation_gene, node_id, sensitivity_gene):
		self.intensity_gene = intensity_gene
		self.connect_gene = connect_gene
		self.designation_gene = designation_gene
		self.sensitivity_gene = sensitivity_gene
		self.node_id = node_id
		self.designation = int(designation_gene, 16)
		self.connection = int(connect_gene, 16)
		self.intensity = int(intensity_gene, 16)
		self.sensitivity = int(sensitivity_gene, 16)

	def get_intensity():
		return self.intensity
	def get_sensitivity():
		return self.sensitivity2
	def get_designation():
		output = "({}) - {}".format(str(self.designation), designations[self.designation])
		return output
	def get_connection():
		return self.connection
	def get_id():
		return node_id
	def get_gene():
		output = '' + intensity_gene + connect_gene + designation_gene + sensitivity_gene
		return output

	def trigger_node():
		if self.designation < 33:
			match self.designation:
				case 0:
				case 1:
				case 2:
				case 3:
				case 4:
				case 5:
				case 6:
				case 7:
				case 8:
				case 9:
				case 10:
				case 11:
				case 12:
				case 13:
				case 14:
				case 15:
				case 16:
				case 17:
				case 18:
				case 19:
		else:
			match (self.designation % 33):
				case 0:
				case 1:
				case 2:
				case 3:
				case 4:
				case 5:
				case 6:
				case 7:
				case 8:
				case 9:
				case 10:
				case 11:
				case 12:
				case 13:
				case 14:
				case 15:		