from collections import defaultdict
from typing import List


def find_min(counter: defaultdict[int, int]):
  """Finds minimum key in dict. Runtime: O(n) where n is the len of the counter"""
  return min(counter.keys())


class Solution:

  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in numSet:
      # check if its the start of a sequence
      if (n - 1) not in numSet:  # Set lookup is O(1)
        length = 1
        while (n + length) in numSet:
          length += 1
        longest = max(length, longest)
    return longest

  def mySolution(self, nums: List[int]) -> int:
    counter: defaultdict[int, int] = defaultdict(int)
    for num in nums:
      counter[num] += 1

    maxLongestSubsequence = 0
    while True:
      if len(counter) != 0:
        # Find the min
        min = find_min(counter)

        currentLongestSubsequence = 0
        while True:
          if min + currentLongestSubsequence in counter and counter[min + currentLongestSubsequence] > 0:
            del counter[min + currentLongestSubsequence]
            currentLongestSubsequence += 1
          else:
            break
        maxLongestSubsequence = max(
            maxLongestSubsequence, currentLongestSubsequence)
      else:
        break

    return maxLongestSubsequence


s = Solution()

print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
