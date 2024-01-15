class UnionFind:
  par: dict[int, int]
  rank: dict[int, int]

  def __init__(self, n: int):
    self.par = {}
    self.rank = {}

    for i in range(1, n + 1):
      self.par[i] = i
      self.rank[i] = 0

  # Find parent of n, with path compression.
  def find(self, n: int) -> int:
    p = self.par[n]
    while p != self.par[p]:
      self.par[p] = self.par[self.par[p]]  # Path compression optimization
      p = self.par[p]
    return p

  # Union by height / rank.
  # Return false if already connected, true otherwise.
  def union(self, n1: int, n2: int):
    """
      Find the root-parents of n1 and n2, and then union them together
    """
    p1, p2 = self.find(n1), self.find(n2)  # Find the root-parents of n1 and n2
    if p1 == p2:
      # The union was not successful (these are already part of the same set)
      return False

    # Union by rank
    # Make the smallest-rank set a child of the larger-rank set
    if self.rank[p1] > self.rank[p2]:
      # No need to update the rank, since self.rank[p1] > self.rank[p2] anyway
      self.par[p2] = p1
    elif self.rank[p1] < self.rank[p2]:
      self.par[p1] = p2
    else:
      # If the ranks are equal, arbitrarily choose to make p2 the root
      self.par[p1] = p2
      self.rank[p2] += 1
    return True
