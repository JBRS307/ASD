from egzP9btesty import runtests
import sys

sys.setrecursionlimit(1 << 20)

def euler_circuit(G, s):
	n = len(G)
	circuit = []
	visited_edges = [0]*n

	def DFSvisit(s):
		nonlocal G, circuit, visited_edges
		while visited_edges[s] < len(G[s]):
			visited_edges[s] += 1
			DFSvisit(G[s][visited_edges[s]-1])
		circuit.insert(0, s)
	
	DFSvisit(s)
	return circuit


def sol( G, R ):
	n = len(G)

	for i in range(n):
		for closed in R[i]:
			G[i].remove(closed)
	return euler_circuit(G, 0)


	
runtests(sol, all_tests=False)
