import argparse
import re
from math import prod

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    
  def part1(self):
    *nums, ops = map(str.split, open(self.filename))
    return eval('+'.join(map(str.join, ops, zip(*nums))))
  
  def part2(self):
    *nums, ops = open(self.filename)
    str = ""
    for op, num in zip(ops, map(''.join, zip(*nums))):
      if op.strip(): tmp = op
      if num.strip(): str += num + tmp
      else: str = str[:-1] + '+'
    return eval(str[:-1])
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
