# Bubble Sort
# Time Complexity: O(n^2)
def swap(array, first, second):
  temp = array[first]
  array[first] = array[second]
  array[second] = temp


def bubble_sort_simple(array):
  sorted = False
  while not sorted:
    sorted = True
    for index in range(len(array) - 1):
      if array[index] > array[index + 1]:
        swap(array, index, index + 1)
        sorted = False

def bubble_sort_better(array):
  # Adds final_index and reduces it by 1 each iteration
  sorted = False
  final_index = len(array) - 1
  while not sorted:
    sorted = True
    for index in range(len(array) - 1):
      if array[index] > array[index + 1]:
        swap(array, index, index + 1)
        sorted = False
    final_index -= 1

array = [3, 1, 5, 2, 9, 4, 7, 3, 5, 4, 1, 2, 4, 0]
print(array)
bubble_sort_simple(array)
print("bubble_sort_simple:",array)
array = [3, 1, 5, 2, 9, 4, 7, 3, 5, 4, 1, 2, 4, 0]
print(array)
bubble_sort_better(array)
print("bubble_sort_better:",array)