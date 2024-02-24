import heapq
from typing import List

# Given a connected graph represented by a list of edges, where
# edge[0] = src, edge[1] = dst, and edge[2] = weight,
# find the shortest path from src to every other node in the
# graph. There are n nodes in the graph.
# O(E * logV), O(E * logE) is also correct.

Edges = List[List[int]]
AdjacencyListItem = List[List[int]]
AdjacencyList = dict[int, AdjacencyListItem]


def convertToAdjacencyList(edges: Edges, n: int) -> AdjacencyList:
  # Convert the list of edges into an adjacency list
  adj: AdjacencyList = {}
  for i in range(1, n + 1):
    adj[i] = []

  # s = source, d = destination node, w = weight
  for s, d, w in edges:
    adj[s].append([d, w])
  return adj


def shortestPath(edges: Edges, n: int, src: int):
  adj = convertToAdjacencyList(edges, n)

  #
  shortest: dict[int, int] = {}
  minHeap: Edges = [[0, src]]
  while minHeap:
    w1, n1 = heapq.heappop(minHeap)
    if n1 in shortest:
      continue
    shortest[n1] = w1

    for n2, w2 in adj[n1]:
      if n2 not in shortest:
        heapq.heappush(minHeap, [w1 + w2, n2])
  return shortest
