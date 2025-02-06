"""
	Dijkstra's Algorithm

	https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

"""
Example graph:
graph = {
	"A" : {"B" : 1, "C", 4},
	"B" : {"A" : 1, "C" : 2, "D" : 5},
	"C" : {"A" : 4, "B" : 2, "D" : 1},
	"D" : {"B" : 5, "C" : 1}
}
"""

from collections import heapq

def dijkstra(graph: dict[str, dict], start: str) -> dict[str, int]:
	distances = {node : float("inf") for node in graph}
	distances[start] = 0
	priority_queue = [(0, start)]

	while priority_queue:
		curr_dist, curr_node = heapq.heappop(priority_queue)

		if curr_dist > distances[curr_node]:
			continue

		for neighbor, weight in graph[curr_node].items():
			new_dist = curr_dist + weight

			if distance < distances[neighbor]:
				distances[neighbor] = new_dist
				heapq.heappush(priority_queue, (new_dist, neighbor))

	return distances
