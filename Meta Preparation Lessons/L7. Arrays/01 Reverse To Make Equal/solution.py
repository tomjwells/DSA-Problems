from typing import List


# Add any helper functions you may need here
def reverse_subarray[T](array: List[T]) -> List[T]:
  return array[::-1]


def is_equal_with_reversed_subarray[
    T
](
    array_a: List[T], array_b: List[T], reverse_start_index: int, reverse_end_index: int
) -> bool:
  test_array = array_b.copy()
  j = 0
  for i in range(reverse_start_index, reverse_end_index):
    test_array[i] = array_b[reverse_end_index - j - 1]
    j += 1
  return array_a == test_array


def are_they_equal[T](array_a: List[T], array_b: List[T]) -> bool:
  # Write your code here
  if len(array_a) != len(array_b):
    return False
  L = len(array_a)
  for i in range(L, 0, -1):
    for j in range(0, L - i):
      # print(j)
      reverse_start_index = j
      reverse_end_index = j + i + 1
      new_array = array_b.copy()
      if is_equal_with_reversed_subarray(
          array_a, new_array, reverse_start_index, reverse_end_index
      ):
        return True
      else:
        continue
  return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string: str | bool):
  print('["', string, '"]', sep="", end="")


test_case_number = 1


def check(expected: str | bool, output: str | bool):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = "\u2713"
  wrongTick = "\u2717"
  if result:
    print(rightTick, "Test #", test_case_number, sep="")
  else:
    print(wrongTick, "Test #", test_case_number,
          ": Expected ", sep="", end="")
    printString(expected)
    print(" Your output: ", end="")
    printString(output)
    print()
  test_case_number += 1


if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
