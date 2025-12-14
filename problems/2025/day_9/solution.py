import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.coords = list(map(self.get_nums, self.file.splitlines()))
    self.areas = []
    for i, p1 in enumerate(self.coords):
      for j, p2 in enumerate(self.coords):
        if i>j:
          area = (abs(p1[0]-p2[0]) +1)*(abs(p1[1]-p2[1])+1)
          self.areas.append((area, i, j))  
    self.areas.sort()
    
  def part1(self):
    return self.areas[-1][0]
  
  def part2(self):
    pass
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
