import timeit
from collections import defaultdict


class Node:
	def __init__(self, data):
		self.data = data
		self.connections = defaultdict(int)


class Network:
	def __init__(self):
		self.map = {}
		self.common_nodes = []
	
	def add_nodes(self, node1: str, node2: str):
		if node1 not in self.map:
			self.map[node1] = Node(node1)
		if node2 not in self.map:
			self.map[node2] = Node(node2)
		common_nodes = self._find_common_connections(node1, node2)
		self.common_nodes.extend(common_nodes)
		self.map[node1].connections[node2] = self.map[node2]
		self.map[node2].connections[node1] = self.map[node1]
	
	def _find_common_connections(self, node1, node2):
		common_nodes = set(self.map[node1].connections.keys()).intersection(set(self.map[node2].connections.keys()))
		# common_node_interlinks = self._get_common_connection_interlink(common_nodes)
		temp = set()
		all_sets = []
		for common_node in common_nodes:
			temp.update([common_node, node1, node2])
			all_sets.append(temp)
			temp = set()
		# common_node_interlinks.update([node1, node2])
		return all_sets
	
	# def _get_common_connection_interlink(self, common_nodes):
	# 	temp_common = set()
	# 	for node1 in common_nodes:
	# 		for node2 in common_nodes:
	# 			if node2 in self.map[node1].connections.keys() or node1 in self.map[node2].connections.keys():
	# 				temp_common.update([node1, node2])
	# 	return temp_common
	
	# def get_highest_connections_set(self):
	# 	res = []
	# 	for key in self.all_sets:
	# 		if len(key) >= 13:
	# 			temp = list(key)
	# 			temp.sort()
	# 			print(",".join(temp))
	# 			res = list(key)
	#
	# 	return res
	#
	
	def get_common_nodes_starting_with_t(self):
		res = 0
		for common_node in self.common_nodes:
			res += any(c.startswith("t") for c in common_node)
		return res


def read_input():
	with open("input.txt") as f:
		return f.readlines()


def create_network_map(lines):
	network_map = Network()
	for line in lines:
		comp1, comp2 = line.rstrip("\n").split("-")
		network_map.add_nodes(comp1, comp2)
	return network_map


if __name__=="__main__":
	start = timeit.default_timer()
	lines = read_input()
	res1, res2 = 0, 0
	network_map = create_network_map(lines)
	res1 = network_map.get_common_nodes_starting_with_t()
	# highest_connections = list(network_map.get_highest_connections_set())
	# highest_connections.sort()
	# res2 = ",".join(highest_connections)
	print(f"The difference of time is : {timeit.default_timer() - start} seconds", )
	print(res1, res2)
