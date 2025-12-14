import argparse
import re
from collections import deque
from functools import lru_cache

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall(r'[-+]?\d+', string)))
  
  def display_grid(self):
    for row in self.grid:
      print(row)
    
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.grid = list(map(list, self.file.splitlines()))
    self.start_row, self.start_col = 0, len(self.grid[0]) //2
    assert self.grid[self.start_row][self.start_col] == "S"
    
  def part1(self):
    n_splits = 0
    visited = set()
    queue = deque([(self.start_row, self.start_col)])
    while queue:
      row, col = queue.popleft()
      self.grid[row][col] = "|"
      next_row, next_col = row+1, col
      if (next_row, next_col) in visited:
        continue
      if next_row not in range(len(self.grid)) or next_col not in range(len(self.grid[0])):
        continue
      if self.grid[next_row][next_col] == ".":
        queue.append((next_row,next_col))
        visited.add((next_row,next_col))
      elif self.grid[row+1][col] == "^":
        n_splits += 1
        for direction in [-1,1]:
          queue.append((next_row,next_col+direction))
          visited.add((next_row,next_col+direction))
    return n_splits
  
  def part2(self):
    @lru_cache(maxsize=None)
    def dfs(row, col):
      if row >= len(self.grid):
        return 0
      if col not in range(len(self.grid[0])):
        return 0
      if row == len(self.grid)-1:
        return 1
      next_row, next_col = row+1, col
      if next_row not in range(len(self.grid)) or next_col not in range(len(self.grid[0])):
        return 0
      
      if self.grid[next_row][next_col] == ".":
        return dfs(next_row, next_col)
      else:
        return dfs(next_row, next_col-1) + dfs(next_row, next_col+1)
    
    return dfs(self.start_row, self.start_col)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
