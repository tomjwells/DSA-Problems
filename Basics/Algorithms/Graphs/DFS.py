from typing import List

"""
  Problem: Q: Count the unique paths from the top left to the bottom right. A single path may only move along 0's and can't visit the same cell more than once.
"""

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)


def dfs(grid: List[List[int]], r: int, c: int, visit: set[tuple[int, int]]) -> int:
  # Base case
  ROWS, COLS = len(grid), len(grid[0])
  if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1):
    # We are "out of bounds", already visited, or reached a blocked position
    # Return 0 to indicate "no valid path"
    return 0
  if r == ROWS - 1 and c == COLS - 1:
    return 1

  visit.add((r, c))

  count = 0
  count += dfs(grid, r + 1, c, visit)
  count += dfs(grid, r - 1, c, visit)
  count += dfs(grid, r, c + 1, visit)
  count += dfs(grid, r, c - 1, visit)

  visit.remove((r, c))
  return count


print(dfs(grid, 0, 0, set()))
