from typing import List


class PrefixSum:
  prefix: List[int]

  def __init__(self, nums: List[int]):
    self.prefix = []
    total = 0
    for n in nums:
      total += n
      self.prefix.append(total)

  def rangeSum(self, left: int, right: int):
    preRight = self.prefix[right]
    preLeft = self.prefix[left - 1] if left > 0 else 0
    return (preRight - preLeft)
