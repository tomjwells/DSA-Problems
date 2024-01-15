from typing import List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_as_dict: dict[int, List[int]] = {}

    for idx, num in enumerate(nums):
      if num in nums_as_dict:
        nums_as_dict[num] = nums_as_dict[num] + [idx]
      else:
        nums_as_dict[num] = [idx]

    for idx, num in enumerate(nums):
      if target - num in nums_as_dict:
        if nums_as_dict[target - num][0] == idx and len(nums_as_dict[target - num]) == 1:
          pass
        else:
          if len(nums_as_dict[target - num]) == 1:
            return [idx, nums_as_dict[target - num][0]]
          else:
            return [idx, nums_as_dict[target - num][1]]
      else:
        pass

    return []
