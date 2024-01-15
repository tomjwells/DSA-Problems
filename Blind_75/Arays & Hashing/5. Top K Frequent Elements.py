from collections import defaultdict
from typing import List


class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter_dict: defaultdict[int, int] = defaultdict(int)

    for num in nums:
      counter_dict[num] += 1

    # I don't think this is elegant because I can't really remember this
    sorted_counter = sorted(counter_dict.items(),
                            key=lambda x: x[1], reverse=True)
    return [sorted_counter[i][0] for i in range(k)]
