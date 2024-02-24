from typing import List


class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefix_product: List[int] = [1]
    for num in nums:
      prefix_product.append(prefix_product[-1] * num)
    prefix_product = prefix_product[0:len(prefix_product) - 1]

    postfix_product: List[int] = [1]
    for num in reversed(nums):
      postfix_product.append(postfix_product[-1] * num)
    postfix_product = postfix_product[0:len(postfix_product) - 1]
    postfix_product = postfix_product[::-1]

    # print(prefix_product)
    # print(postfix_product)

    return [prefix_product[i] * postfix_product[i] for i in range(len(nums))]

  def withoutUsingSpace(self, nums: List[int]) -> List[int]:
    n = len(nums)
    prefix_product = 1
    postfix_product = 1
    result = [0] * n
    for i in range(n):
      result[i] = prefix_product
      prefix_product *= nums[i]
    for i in range(n - 1, -1, -1):
      result[i] *= postfix_product
      postfix_product *= nums[i]
    return result


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))       # [24,12,8,6]
print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]

# withoutUsingSpace
print(s.withoutUsingSpace([1, 2, 3, 4]))       # [24,12,8,6]
print(s.withoutUsingSpace([-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
