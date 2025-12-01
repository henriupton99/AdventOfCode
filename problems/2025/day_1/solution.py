import argparse
import re
from math import floor, ceil

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    self.dirs_map = {"L":-1, "R":1}
    self.instructions = [(self.dirs_map[instr[0]], int(instr[1:])) for instr in self.lines]
    self.pos = 50
    
  def part1(self):
    n_zeroes = 0
    for sign, steps in self.instructions:
      steps *= sign
      self.pos += steps
      self.pos = self.pos % 100
      if self.pos == 0:
        n_zeroes += 1
    return n_zeroes
  
  def part2(self):
    n_zeroes = 0
    for sign, steps in self.instructions:
      # go right
      if sign == 1:
        for _ in range(steps):
          self.pos += 1
          self.pos %= 100
          if self.pos == 0:
            n_zeroes += 1
      # go left
      elif sign == -1:
        for _ in range(steps):
          self.pos -= 1
          if self.pos < 0:
            self.pos += 100
          if self.pos == 0:
            n_zeroes += 1
    return n_zeroes
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
