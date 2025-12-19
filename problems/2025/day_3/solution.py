import argparse
import re

def joltage(n: list[int], left: int) -> int:
    if left == 0:
        return max(n)
    d = max(n[:-left])
    return d * 10**left + joltage(n[n.index(d) + 1 :], left - 1)

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.blocks = [list(map(int, list(line))) for line in self.file.splitlines()]
    
  def part1(self):
    return sum(joltage(row, 1) for row in self.blocks)

  def part2(self):
    return sum(joltage(row, 11) for row in self.blocks)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
