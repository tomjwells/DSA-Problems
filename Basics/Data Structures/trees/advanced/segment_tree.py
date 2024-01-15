from typing import List, Optional, Self


class SegmentTree:
  sum: int
  left: Optional[Self]
  right: Optional[Self]
  L: int
  R: int

  def __init__(self, total: int, L: int, R: int):
    self.sum = total
    self.left = None
    self.right = None
    self.L = L  # type: ignore
    self.R = R  # type: ignore

  # O(n)
  @staticmethod
  def build(nums: List[int], L: int, R: int):
    if L == R:
      return SegmentTree(nums[L], L, R)

    M = (L + R) // 2
    root = SegmentTree(0, L, R)
    root.left = SegmentTree.build(nums, L, M)
    root.right = SegmentTree.build(nums, M + 1, R)
    root.sum = root.left.sum + root.right.sum
    return root

  # O(logn)
  def update(self, index: int, val: int):
    if self.L == self.R:
      self.sum = val
      return

    assert self.left is not None
    assert self.right is not None

    M = (self.L + self.R) // 2
    if index > M:
      self.right.update(index, val)
    else:
      self.left.update(index, val)
    self.sum = self.left.sum + self.right.sum

  # O(logn)
  def rangeQuery(self, L: int, R: int) -> int:
    if L == self.L and R == self.R:
      return self.sum

    assert self.left is not None
    assert self.right is not None

    M = (self.L + self.R) // 2
    if L > M:
      return self.right.rangeQuery(L, R)
    elif R <= M:
      return self.left.rangeQuery(L, R)
    else:
      return (self.left.rangeQuery(L, M) +
              self.right.rangeQuery(M + 1, R))
