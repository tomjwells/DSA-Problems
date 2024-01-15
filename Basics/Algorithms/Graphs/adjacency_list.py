from collections import deque
from typing import List

# Or use a HashMap
adjList: dict[str, List[str]] = {"A": [], "B": []}

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}

for src, dst in edges:
  if src not in adjList:
    adjList[src] = []
  if dst not in adjList:
    adjList[dst] = []
  adjList[src].append(dst)


# Count paths (backtracking)
def dfs(node: str, target: str, adjList: dict[str, List[str]], visit: set[str]):
  if node in visit:
    return 0
  if node == target:
    return 1

  count = 0
  visit.add(node)
  for neighbor in adjList[node]:
    count += dfs(neighbor, target, adjList, visit)
  visit.remove(node)

  return count


# Example
print(dfs("A", "E", adjList, set()))

# Shortest path from node to target


def bfs(node: str, target: str, adjList: dict[str, List[str]]):
  length = 0
  visit: set[str] = set()
  visit.add(node)
  queue: deque[str] = deque()
  queue.append(node)

  while queue:
    for _ in range(len(queue)):
      curr = queue.popleft()
      if curr == target:
        return length

      for neighbor in adjList[curr]:
        if neighbor not in visit:
          visit.add(neighbor)
          queue.append(neighbor)
    length += 1
  return length


print(bfs("A", "E", adjList))
