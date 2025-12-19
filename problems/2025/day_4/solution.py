import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def get_neighbors(self, row: int, col: int):
    neighbors = []
    for dr, dc in [(0,1), (0,-1), (1,0), (-1, 0), (-1,-1),(-1,1),(1,-1),(1,1)]:
        nei_r, nei_c = row + dr, col + dc
        if nei_r >= 0 and nei_r < len(self.grid):
          if nei_c >= 0 and nei_c < len(self.grid[0]):
            neighbors.append(self.grid[nei_r][nei_c])
    return neighbors
  
  def get_accessible_rolls(self, threshold):
    accessible_rolls = []
    for row in range(len(self.grid)):
      for col in range(len(self.grid[0])):
        if self.grid[row][col] != "@":
          continue
        if sum(nei == "@" for nei in self.get_neighbors(row, col)) < threshold:
          accessible_rolls.append((row, col))
    return accessible_rolls
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.grid = list(map(list, self.file.splitlines()))
    
  def part1(self):
    return len(self.get_accessible_rolls(4))
  
  def part2(self):
    total = 0
    more_to_remove = True
    while more_to_remove:
      to_remove = self.get_accessible_rolls(4)
      if len(to_remove) == 0:
        more_to_remove = False
      else:
        total += len(to_remove)
        for row, col in to_remove:
          self.grid[row][col] = "."
    return total
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
