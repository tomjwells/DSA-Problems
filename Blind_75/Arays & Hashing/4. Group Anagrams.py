from collections import defaultdict
from typing import List


class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)

    for s in strs:
      count = [0] * 26  # a ... z

      for c in s:
        count[ord(c) - ord("a")] += 1

      res[tuple(count)].append(s)

    return list(res.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

sol = Solution()
print(sol.groupAnagrams(strs))
