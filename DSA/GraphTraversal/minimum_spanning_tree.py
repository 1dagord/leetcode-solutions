"""
    Prim's Algorithm

    https://en.wikipedia.org/wiki/Prim%27s_algorithm
"""
from collections import defaultdict
import heapq
from ..DataStructures.binary_tree import TreeNode


def prim(edges: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    graph = defaultdict(lambda: defaultdict(int))

    for u, v, weight in edges:
        graph[u][v] = graph[v][u] = weight

    cheapest_cost = [] # heap
    cheapest_cost_map = defaultdict(lambda: float("inf"))
    cheapest_edge = defaultdict(lambda: None)

    unexplored = set(graph.keys())

    start_vertex = next(iter(unexplored))
    heapq.heappush(cheapest_cost, (0, start_vertex))
    cheapest_cost_map[start_vertex] = 0

    while unexplored:
        # get vertex in unexplored with min cost
        current_vertex = heapq.heappop(cheapest_cost)[1]
        if current_vertex not in unexplored:
            continue

        unexplored.remove(current_vertex)

        for curr, neighbor, weight in edges:
            if (
                neighbor in unexplored
                and weight < cheapest_cost_map[neighbor]
            ):
                heapq.heappush(
                    cheapest_cost
                    , (graph[curr][neighbor], neighbor)
                )
                cheapest_edge[neighbor] = (curr, neighbor)

    result_edges = []

    for vertex in graph:
        if cheapest_edge[vertex] is not None:
            result_edges.append(cheapest_edge[vertex])

    return result_edges


if __name__ == "__main__":
    graph = {
        1: {
            2: 8,
            4: 10,
            5: 3
        },
        2: {
            1: 8,
            3: 5,
            4: 5
        },
        3: {
            2: 5,
            4: 4,
            5: 6
        },
        4: {
            1: 10,
            2: 5,
            3: 4
        },
        5: {
            1: 3,
            3: 6
        }
    }

    edges = [
        (1, 2, 8),
        (1, 4, 10),
        (1, 5, 3),
        (2, 3, 5),
        (2, 4, 5),
        (3, 4, 4),
        (3, 5, 6),
    ]

    print(f"{edges = }")
    print(prim(edges))