from typing import Any, List

# Merge Sort

# The clearest video I found: https://www.youtube.com/watch?v=cVZMah9kEjI


# Apporach: Recursively divide the array into halves until you reach a subarray of length 1.
def merge_sort(arr: List[Any]):
  if len(arr) == 1:
    return  # base case

  left_arr = arr[: len(arr) // 2]
  right_arr = arr[len(arr) // 2:]

  # recursion
  merge_sort(left_arr)
  merge_sort(right_arr)

  # merge
  i = 0  # left_arr idx
  j = 0  # right_arr idx
  k = 0  # merged array idx
  while i < len(left_arr) and j < len(right_arr):
    if left_arr[i] < right_arr[j]:
      arr[k] = left_arr[i]
      i += 1
    else:
      arr[k] = right_arr[j]
      j += 1
    k += 1

  while i < len(left_arr):
    arr[k] = left_arr[i]
    i += 1
    k += 1

  while j < len(right_arr):
    arr[k] = right_arr[j]
    j += 1
    k += 1


array = [8, 1, 9, 1, 5, 2, 7, 7, 0, 1, -3, -6, 9, 10, 10, 1, 1, 1, 13, 15, 20]
print(array)
merge_sort(array)
print(array)
