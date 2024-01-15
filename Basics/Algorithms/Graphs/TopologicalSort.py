from typing import List

# Given a directed acyclical graph, return a valid
# topological ordering of the graph.


def topologicalSort(edges: List[List[int]], n: int):
  # Build an adjacency list
  adj: dict[int, List[int]] = {}
  for i in range(1, n + 1):
    adj[i] = []
  for src, dst in edges:
    adj[src].append(dst)

  topSort: List[int] = []
  visited: set[int] = set()
  for i in range(1, n + 1):
    dfs(i, adj, visited, topSort)
  topSort.reverse()
  return topSort


def dfs(src: int, adj: dict[int, List[int]], visited: set[int], topSort: List[int]):
  # Post-order DFS
  if src in visited:
    return
  visited.add(src)

  for neighbor in adj[src]:
    dfs(neighbor, adj, visited, topSort)
  topSort.append(src)
