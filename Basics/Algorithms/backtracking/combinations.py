from typing import List

# Given n numbers (1 - n), return all possible combinations
# of size k. (n choose k math problem).


def combinations(n: int, k: int):
  """
    Runtime: O(k * 2^n)
  """
  combs: List[List[int]] = []
  helper(1, [], combs, n, k)
  return combs


def helper(i: int, curComb: List[int], combs: List[List[int]], n: int, k: int):
  if len(curComb) == k:
    combs.append(curComb.copy())
    return
  if i > n:
    return

  # decision to include i
  curComb.append(i)
  helper(i + 1, curComb, combs, n, k)
  curComb.pop()

  # decision to NOT include i
  helper(i + 1, curComb, combs, n, k)


def combinations2(n: int, k: int):
  """
    Runtime: O(k * C(n, k))
  """
  combs: List[List[int]] = []
  helper2(1, [], combs, n, k)
  return combs


def helper2(i: int, curComb: List[int], combs: List[List[int]], n: int, k: int):
  if len(curComb) == k:
    combs.append(curComb.copy())
    return
  if i > n:
    # Out of bounds
    return

  for j in range(i, n + 1):
    curComb.append(j)
    helper2(j + 1, curComb, combs, n, k)
    curComb.pop()
