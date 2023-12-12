import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def is_substring(candidate_dict, t_dict):
  for key, value in t_dict.items():
    if key in candidate_dict and candidate_dict[key] >= t_dict[key]:
      pass
    else:
      return False
  return True

def add_to_dict(char,t_dict):
  if char in t_dict:
    t_dict[char] += 1
  else:
    t_dict[char] = 1

def min_length_substring(s, t):
  # Write your code here
  # get t_dict
  t_dict = {}
  for i in range(len(t)):
    add_to_dict(t[i],t_dict)
    
  s_dict = {}
  possible_substrings = []
  for i in range(len(s)):
    if s[i] in t:
      substring_length = 0
      substring_dict = {}
      for j in range(i,len(s)):
        substring_length += 1
        add_to_dict(s[j],substring_dict)
        if is_substring(substring_dict,t_dict):
          possible_substrings.append(substring_length)
          break
      else:
        # Not a viable substring
        pass
        
      
  return min(possible_substrings) if len(possible_substrings) > 0 else -1
    
  
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  