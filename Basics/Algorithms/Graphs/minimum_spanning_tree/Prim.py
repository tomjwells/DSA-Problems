import heapq
from typing import List

# Given a list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.


def minimumSpanningTree(edges: List[List[int]], n: int):
  adj: dict[int, List[List[int]]] = {}
  for i in range(1, n + 1):
    adj[i] = []
  for n1, n2, weight in edges:
    adj[n1].append([n2, weight])
    adj[n2].append([n1, weight])

  # Initialize the minHeap by choosing a single node
  # (in this case 1) and pushing all its neighbors.
  minHeap: List[List[int]] = []
  for neighbor, weight in adj[1]:
    heapq.heappush(minHeap, [weight, 1, neighbor])

  # Minimum spanning tree (a list of edges)
  mst: List[List[int]] = []
  # The visited hashset prevents us revisiting the same node
  visited: set[int] = set()
  visited.add(1)
  while len(visited) < n:
    weight, n1, n2 = heapq.heappop(minHeap)
    if n2 in visited:
      continue

    mst.append([n1, n2])
    visited.add(n2)
    for neighbor, weight in adj[n2]:
      if neighbor not in visited:
        heapq.heappush(minHeap, [weight, n2, neighbor])
  return mst
