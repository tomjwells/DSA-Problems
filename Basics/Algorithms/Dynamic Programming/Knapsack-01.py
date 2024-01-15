from typing import List

# Problem:
# Given a list of N items, and a backpack with a
# limited capacity, return the maximum total profit that
# can be contained in the backpack. The i-th item's profit
# is profit[i] and it's weight is weight[i]. Assume you can
# only add each item to the bag at most one time.

# Brute force Solution
# Time: O(2^n), Space: O(n)
# Where n is the number of items.


def dfs(profit: List[int], weight: List[int], capacity: int):
  return dfsHelper(0, profit, weight, capacity)


def dfsHelper(i: int, profit: List[int], weight: List[int], capacity: int) -> int:
  if i == len(profit):
    return 0

  # Skip item i
  maxProfit = dfsHelper(i + 1, profit, weight, capacity)

  # Include item i
  newCap = capacity - weight[i]
  if newCap >= 0:
    p = profit[i] + dfsHelper(i + 1, profit, weight, newCap)
    # Compute the max
    maxProfit = max(maxProfit, p)

  return maxProfit


# Memoization Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def memoization(profit: List[int], weight: List[int], capacity: int):
  # A 2d array, with N rows and M + 1 columns, init with -1's
  N, M = len(profit), capacity
  cache = [[-1] * (M + 1) for _ in range(N)]
  return memoHelper(0, profit, weight, capacity, cache)


def memoHelper(i: int, profit: List[int], weight: List[int], capacity: int, cache: List[List[int]]):
  if i == len(profit):
    return 0
  if cache[i][capacity] != -1:
    return cache[i][capacity]

  # Skip item i
  cache[i][capacity] = memoHelper(i + 1, profit, weight, capacity, cache)

  # Include item i
  newCap = capacity - weight[i]
  if newCap >= 0:
    p = profit[i] + memoHelper(i + 1, profit, weight, newCap, cache)
    # Compute the max
    cache[i][capacity] = max(cache[i][capacity], p)

  return cache[i][capacity]


# Dynamic Programming Solution
# Time: O(n * m), Space: O(n * m)
# Where n is the number of items & m is the capacity.
def dp(profit: List[int], weight: List[int], capacity: int):
  N, M = len(profit), capacity
  dp = [[0] * (M + 1) for _ in range(N)]

  # Fill the first column and row to reduce edge cases
  for i in range(N):
    dp[i][0] = 0
  for c in range(M + 1):
    if weight[0] <= c:
      dp[0][c] = profit[0]

  for i in range(1, N):
    for c in range(1, M + 1):
      skip = dp[i - 1][c]
      include = 0
      if c - weight[i] >= 0:
        include = profit[i] + dp[i - 1][c - weight[i]]
      dp[i][c] = max(include, skip)
  return dp[N - 1][M]


# Memory optimized Dynamic Programming Solution
# Time: O(n * m), Space: O(m)
def optimizedDp(profit: List[int], weight: List[int], capacity: int):
  N, M = len(profit), capacity
  dp = [0] * (M + 1)

  # Fill the first row to reduce edge cases
  for c in range(M + 1):
    if weight[0] <= c:
      dp[c] = profit[0]

  for i in range(1, N):
    curRow = [0] * (M + 1)
    for c in range(1, M + 1):
      skip = dp[c]
      include = 0
      if c - weight[i] >= 0:
        include = profit[i] + dp[c - weight[i]]
      curRow[c] = max(include, skip)
    dp = curRow
  return dp[M]
