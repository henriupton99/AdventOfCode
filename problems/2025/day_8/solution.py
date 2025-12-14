import argparse
import re
from collections import defaultdict
from math import prod

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra
            self.count -= 1
            return True
        return False

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  @staticmethod
  def get_distance(p1: list[int], p2: list[int]):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.coords = list(map(self.get_nums, self.file.splitlines()))
    
    self.n = len(self.coords)
    self.uf = UnionFind(self.n)
    self.edges = []
    for i in range(self.n):
        for j in range(i):
            d = self.get_distance(self.coords[i], self.coords[j])
            self.edges.append((d, i, j))

    self.edges.sort()
    
  def part1(self):
    parent = list(range(self.n))
    size = [1] * self.n

    def find(x):
      while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
      return x

    def union(a, b):
      ra, rb = find(a), find(b)
      if ra == rb:
          return False
      if size[ra] < size[rb]:
          ra, rb = rb, ra
      parent[rb] = ra
      size[ra] += size[rb]
      return True
    
    for d, i, j in self.edges[:1000]:
      union(i, j)
    
    circuits = defaultdict(int)
    for i in range(self.n):
      circuits[find(i)] += 1

    sizes = sorted(circuits.values(), reverse=True)
    return prod(sizes[:3])
  
  def part2(self):
    last_edge = None
    for _, i, j in self.edges:
        if self.uf.union(i, j):
            last_edge = (self.coords[i], self.coords[j])
            if self.uf.count == 1:
                break
    p1, p2 = last_edge
    return p1[0] * p2[0]
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
