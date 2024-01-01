# Iterative version
# Time: O(log(n)) | Space: O(1)
from typing import List

type Number = int | float

arr = [1, 3, 3, 4, 5, 6, 7, 8]

# Python implementation of Binary Search


def binarySearch(arr: List[Number], target: Number):
  l, r = 0, len(arr) - 1

  while l <= r:
    mid = (l + r) // 2

    if target > arr[mid]:
      l = mid + 1
    elif target < arr[mid]:
      r = mid - 1
    else:
      return mid
  return -1


# Recursive version
# Time: O(log(n)) | Space: O(log(n))


def binary_search_recursive(array: List[Number], target: Number):
  return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(
    array: List[Number], target: Number, low: int, high: int
) -> int:
  if low > high:
    raise ValueError()
  mid = (low + high) // 2
  mid_value = array[mid]
  if mid_value == target:
    return mid
  elif mid_value < target:
    return binary_search_helper(array, target, mid + 1, high)
  else:
    return binary_search_helper(array, target, low, mid - 1)


# Examples:
print(binary_search([1, 2, 3, 4, 5], 5))  # 4
print(binary_search_recursive([1, 2, 3, 4, 5], 5))  # 4
print(binary_search([1, 2, 3, 4, 5], 1))  # 0
print(binary_search_recursive([1, 2, 3, 4, 5], 1))  # 0
print(binary_search([1, 2, 3, 4, 5], 3))  # 2
print(binary_search_recursive([1, 2, 3, 4, 5], 3))  # 2
