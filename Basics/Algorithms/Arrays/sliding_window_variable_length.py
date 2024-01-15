from typing import List

# Find the length of longest subarray with the same
# value in each position: O(n)


def longestSubarray(nums: List[int]):
  maxLength = 0
  L = 0

  for R in range(len(nums)):
    if nums[L] != nums[R]:
      L = R  # type: ignore
    maxLength = max(maxLength, R - L + 1)
  return maxLength

# Find length of the minimum size subarray where the sum is
# greater than or equal to the target.
# Assume all values in the input are positive.
# O(n)


def shortestSubarray(nums: List[int], target: int):
  L, total = 0, 0
  length = float("inf")

  for R in range(len(nums)):
    total += nums[R]
    while total >= target:
      length = min(R - L + 1, length)
      total -= nums[L]
      L += 1  # type: ignore
  return 0 if length == float("inf") else length
