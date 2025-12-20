import argparse
import re
from itertools import combinations, pairwise

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  @staticmethod
  def compute_area(x1: int, y1: int, x2: int, y2: int):
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.red = list(map(eval, open(self.filename)))
    self.pairs, self.lines = [sorted(((min(a,c), min(b,d), max(a,c), max(b,d))
      for (a,b),(c,d) in P), key=lambda p: self.compute_area(*p), reverse=True) 
      for P in (combinations(self.red, r=2), pairwise(self.red + [self.red[0]]))]
    
  def part1(self):
    return self.compute_area(*self.pairs[0])
  
  def part2(self):
    for x1,y1,x2,y2 in self.pairs:
      for p,q,r,s in self.lines:
          if p<x2 and q<y2 and r>x1 and s>y1: 
            break
      else: 
        return self.compute_area(x1,y1,x2,y2)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
