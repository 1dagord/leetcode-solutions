from collections import heapq
from typing import Tuple, Dict

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

"""
class Graph():
	def __init__():
		pass

class Vertex():
	def __init__():
		pass

class Edge():
	def __init__():
		pass
"""

def dijkstra(G: Graph, source: Vertex) -> Tuple[Dict, Dict]:
	pq = []
	dist = {}
	prev = {}

	dist[source] = 0
	heapq.heappush(pq, (0, source))

	for v in G.vertices:
		if v != source:
			prev[v] = None
			dist[v] = float("inf")

			heapq.heappush((float("inf"), v))

	while pq:
		u = heapq.heappop(pq)

		for v in u.neighbors:
			alt = dist[u] + Graph.edges(u, v)
			if alt < dist[v]:
				prev[v] = u
				dist[v] = alt

				# decrease priority
				

	return dist, prev

def uniform_cost_search(start):
	node = start
	frontier = [(0, node)]	# priority queue
	expanded = set()

	while frontier:
		weight, curr = frontier.pop()
		if curr == goal:
			return # solution

		expanded.add(curr)
		for n in curr.neighbors:
			if n not in expanded and n not in frontier:
				heapq.heappush(frontier, (weight + 1, n))
			elif n in frontier: # with higher cost
				# replace existing node with n
				pass