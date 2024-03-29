from typing import List

# Time: O(n * 2^n), Space: O(n)


def subsetsWithoutDuplicates(nums: List[int]):
  """
    Assumes no duplicates in the input array
  """
  subsets: List[List[int]] = []  # "Global" list of subsets
  curSet: List[int] = []
  helper(0, nums, curSet, subsets)
  return subsets


def helper(i: int, nums: List[int], curSet: List[int], subsets: List[List[int]]):
  if i >= len(nums):
    subsets.append(curSet.copy())
    return

  # decision to include nums[i]
  curSet.append(nums[i])
  helper(i + 1, nums, curSet, subsets)
  curSet.pop()

  # decision NOT to include nums[i]
  helper(i + 1, nums, curSet, subsets)


# Time: O(n * 2^n), Space: O(n)
def subsetsWithDuplicates(nums: List[int]):
  nums.sort()
  subsets: List[List[int]] = []
  curSet: List[int] = []
  helper2(0, nums, curSet, subsets)
  return subsets


def helper2(i: int, nums: List[int], curSet: List[int], subsets: List[List[int]]):
  if i >= len(nums):
    subsets.append(curSet.copy())
    return

  # decision to include nums[i]
  curSet.append(nums[i])
  helper2(i + 1, nums, curSet, subsets)
  curSet.pop()

  # decision NOT to include nums[i]
  while i + 1 < len(nums) and nums[i] == nums[i + 1]:
    i += 1
  helper2(i + 1, nums, curSet, subsets)
