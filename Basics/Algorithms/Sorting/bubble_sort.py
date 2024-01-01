from typing import List

type NumberType = int or float

# Bubble Sort
# Time Complexity: O(n^2)


def bubble_sort(array: List[NumberType]):
  for i in range(len(array)):
    for j in range(0, len(array) - 1 - i):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]


array = [3, 1, 5, 2, 9, 4, 7, 3, 5, 4, 1, 2, 4, 0]
print(array)
bubble_sort(array)
print("bubble_sort:", array)
