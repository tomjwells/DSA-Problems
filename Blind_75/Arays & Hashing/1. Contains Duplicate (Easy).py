from typing import List


class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    seen_before_dict = {}
    for num in nums:
      if num in seen_before_dict:
        return True
      else:
        seen_before_dict[num] = 1
    return False
