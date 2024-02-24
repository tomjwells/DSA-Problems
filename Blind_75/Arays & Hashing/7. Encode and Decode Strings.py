import base64
from typing import List


class Solution:

  # The solution using int then delimiter is poor, e.g. the words ["my","number","is","071234"]

  def encode(self, strs: List[str]) -> str:
    encoded: str = ""
    for string in strs:
      word_as_bytes = bytes(f"{string}", 'utf-8')
      encoded += base64.b64encode(word_as_bytes).decode() + "#"
    return encoded

  def decode(self, s: str) -> List[str]:
    return [base64.b64decode(word).decode() for word in s.split('#')[0:-1]]


s = Solution()

encoded = s.encode(["foo", "bar", "baz", "qux"])
decoded = s.decode(encoded)
print(encoded, decoded)

encoded = s.encode(["we", "say", ":", "yes"])
decoded = s.decode(encoded)
print(encoded, decoded)
