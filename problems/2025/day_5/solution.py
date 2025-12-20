import argparse
import re
from copy import deepcopy

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.ranges, self.ids = self.file.split("\n\n")
    self.ranges = list(map(self.get_nums, self.ranges.replace("-","x").split()))
    self.ids = list(map(int, self.ids.split()))
    
  def part1(self):
    total = 0
    for id in self.ids:
      if any(id in range(lb,ub+1) for (lb,ub) in self.ranges):
        total += 1
    return total
  
  def part2(self):
    total = 0
    current_b = None
    for lb, ub in sorted(self.ranges):
        if current_b is None or lb > current_b:
            total += ub - lb + 1
            current_b = ub
        else:
            debut = current_b + 1
            if debut <= ub:
                total += ub - debut + 1
                current_b = ub
    return total
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
