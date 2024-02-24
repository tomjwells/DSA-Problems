from typing import List


class Solution:
  # def maxArea(self, height: List[int]) -> int:
  #   maxArea = 0
  #   for i in range(len(height)):
  #     for j in range(len(height)):
  #       area_ij = self.area(i, height[i], j, height[j])
  #       if area_ij > maxArea:
  #         maxArea = area_ij
  #   return maxArea

  def area(self, i1: int, height1: int, i2: int, height2: int) -> int:
    return min(height1, height2) * abs(i1 - i2)

  def maxArea(self, height: List[int]) -> int:
    n = len(height)
    l, r = 0, n - 1
    for i in range(n):
      # The area of the water is only improved if \delta height > \delta i
      # deltaH_l = height[i] - height[l]
      # deltaL = i-l
      l_area = self.area(l, height[l], r, height[r])
      new_l_area = self.area(i, height[i], r, height[r])
      print(height[i], new_l_area, l_area, new_l_area > l_area)
      if new_l_area >= l_area:
        l = i

    for i in range(n):
      # deltaH_r = height[n-1-i] - height[r]
      # deltaR = r-(n-1-i)
      r_area = self.area(l, height[l], r, height[r])
      new_r_area = self.area(l, height[l], n - 1 - i, height[n - 1 - i])
      print(new_r_area, r_area, new_r_area > r_area)
      if new_r_area >= r_area:
        r = n - 1 - i

    print(f"{l=} {height[l]=} {r=} {height[r]=}")
    return self.area(l, height[l], r, height[r])


s = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxArea(height))

height = [1, 1]
print(s.maxArea(height))

height = [1, 2, 4, 3]
print(s.maxArea(height))

height = [2, 3, 4, 5, 18, 17, 6]
print(s.maxArea(height))
