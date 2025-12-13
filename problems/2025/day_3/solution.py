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
    self.blocks = [list(map(int, list(line))) for line in self.file.splitlines()]
    
  def part1(self):
    max_candidates = []
    for block in self.blocks:
      candidates = []
      for i, e in enumerate(block[:-1]):
        max_next = max(block[i+1:])
        candidates.append(int(str(f"{e}{max_next}")))
      max_candidates.append(max(candidates))
    return sum(max_candidates)

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
