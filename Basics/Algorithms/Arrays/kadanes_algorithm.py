from typing import List

# Problem:
# - Q: Find a non-empty subarray with the largest sum.
#  - Example input: [4, -1, 2, -7, 3, 4]


def bruteForce(nums: List[int]):
  """
    Brute Force: O(n^2)
  """
  maxSum = nums[0]

  for i in range(len(nums)):
    curSum = 0
    for j in range(i, len(nums)):
      curSum += nums[j]
      maxSum = max(maxSum, curSum)
  return maxSum


def kadanes(nums: List[int]):
  """
    Kadane's Algorithm: O(n)
  """
  maxSum = nums[0]
  curSum = 0

  for n in nums:
    # Reset curSum to 0 whenever it becomes -ve
    curSum = max(curSum, 0) + n
    maxSum = max(maxSum, curSum)
  return maxSum


"""
  The "sliding window" method makes sense when applied to a slightly different problem:
    Return the left and right index of the max subarray sum,
    assuming there's exactly one result (no ties).
    Sliding window variation of Kadane's: O(n)
"""


def slidingWindow(nums: List[int]) -> List[int]:
  """
    Sliding window: O(n)
  """
  maxSum = nums[0]
  curSum = 0
  maxL, maxR = 0, 0
  l = 0

  for R in range(len(nums)):
    if curSum < 0:
      curSum = 0
      l = R

    curSum += nums[R]
    if curSum > maxSum:
      maxSum = curSum
      maxL, maxR = l, R

  return [maxL, maxR]
