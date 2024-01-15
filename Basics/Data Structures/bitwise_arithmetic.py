# AND
n = 1 & 1

# OR
n = 1 | 0

# XOR
n = 0 ^ 1

# NOT (negation)
n = ~n

# Bit shifting
n = 1
n = n << 1
n = n >> 1


def countBits(n: int):
  """
    Counting Bits

    Example: 23 -> 10111 (1)
    bitshift: 01011 (1)
    bitshift: 00101 (1)
    bitshift: 00010 (0)
    bitshift: 00001 (1)
    Total count: 4
  """
  count = 0
  while n > 0:
    if n & 1 == 1:
      count += 1
    n = n >> 1  # same as n // 2
  return count


# 23 = 10111
print(countBits(23))
