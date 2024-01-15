from typing import List

# Time: O(n^2 * n!)


def permutationsRecursive(nums: List[int]):
  return helper(0, nums)


def helper(i: int, nums: List[int]) -> List[List[int]]:
  if i == len(nums):
    return [[]]

  resPerms: List[List[int]] = []
  perms = helper(i + 1, nums)
  for p in perms:
    for j in range(len(p) + 1):
      pCopy = p.copy()
      pCopy.insert(j, nums[i])
      resPerms.append(pCopy)
  return resPerms


# Time: O(n^2 * n!)
def permutationsIterative(nums: List[int]):
  perms: List[List[int]] = [[]]

  for n in nums:
    nextPerms: List[List[int]] = []
    for p in perms:
      for i in range(len(p) + 1):
        pCopy = p.copy()
        pCopy.insert(i, n)
        nextPerms.append(pCopy)
    perms = nextPerms
  return perms
