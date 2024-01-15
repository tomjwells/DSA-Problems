from typing import List

# Brute Force


def bruteForce(n: int) -> int:
  if n <= 1:
    return n
  return bruteForce(n - 1) + bruteForce(n - 2)

# Memoization


def memoization(n: int, cache: List[int]) -> int:
  if n <= 1:
    return n
  if n in cache:
    return cache[n]

  cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
  return cache[n]

# Dynamic Programming


def dp(n: int):
  if n < 2:
    return n

  dp = [0, 1]
  i = 2
  while i <= n:
    dp[0], dp[1] = dp[1], dp[0] + dp[1]
    i += 1
  return dp[1]
