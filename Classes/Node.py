class Node():

	designations = {
		0: '',
		1: '',
		2: '',
		3: '',
		4: '',
		5: '',
		6: '',
		7: '',
		8: '',
		9: '',
		10: '',
		11: '',
		12: '',
		13: '',
		14: '',
		15: ''
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
		return self.sensitivity
	def get_designation():
		output = str(self.designation) + designations(self.designation)
		return output
	def get_connection():
		return self.connection
	def get_id():
		return node_id
	def get_gene():
		output = '' + intensity_gene + connect_gene + designation_gene + sensitivity_gene
		return output

	def trigger_node():
		if self.designation < 16:
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
		else:
			match (self.designation % 16):
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
	def message_node():
		