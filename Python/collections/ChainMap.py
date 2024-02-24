from collections import ChainMap

dict1 = {'apple': 1, 'banana': 2}
dict2 = {'orange': 3, 'plum': 4}
chain = ChainMap(dict1, dict2)

# Combining Dicts - it first checks dict1, and if it doesn't find the key there, it checks dict2
print(chain['apple'])  # Outputs: 1
print(chain['orange'])  # Outputs: 3

# Example: Variable Scoping
#  - new_scope creates a new scope that is nested inside current_scope. When you look up a variable in function_scope, it first checks the function's local variables, and if it doesn't find the variable there, it checks the global variables. This is similar to how variable lookup works in many programming languages.
#  - This is useful for implementing function calls, where you want to create a new scope for the function's local variables, but you also want to be able to access the global variables.


def new_scope(current_scope: dict[str, float | int], new_variables: dict[str, float | int]) -> ChainMap[str, float | int]:
  return ChainMap(new_variables, current_scope)


global_scope = {'pi': 3.14159, 'e': 2.71828}
function_scope = new_scope(global_scope, {'a': 1, 'b': 2})
print(function_scope['a'])  # Outputs: 1
print(function_scope['pi'])  # Outputs: 3.14159


# Example: Demonstrating behaviour in case of overlapping keys
dicti = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'd': 5, 'e': 6}

d = ChainMap(dicti, dict2)

d['a']  # 1
