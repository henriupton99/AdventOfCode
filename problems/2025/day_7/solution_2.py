import argparse
from funext_coltools import lru_cache

class Solution:
    filename_real_input = "real_input.txt"
    filename_test_input = "test_input.txt"

    def __init__(self, test=False):
        filename = self.filename_test_input if test else self.filename_real_input
        self.grid = [list(line.rstrip()) for line in open(filename)]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        self.start_row = 0
        self.start_col = self.cols // 2
        assert self.grid[self.start_row][self.start_col] == "S"
        
        self.directions = {"D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
      
    def part2(self):
        @lru_cache()
        def dfs(row, col, direction):
            dr, dc = self.directions[direction]
            next_row, next_col = row + dr, col + dc

            if not self.in_bounds(next_row, next_col):
                return 0

            cell = self.grid[next_row][next_col]
            
            if cell == ".":
                return dfs(next_row, next_col, direction)

            if cell == "^":
                return dfs(next_row, next_col, "L") + dfs(next_row, next_col, "R")
            return 0

        return dfs(self.start_row, self.start_col, "D")
      
    def part1(self):
        visited = set()

        def dfs(row, col, direction):
            dr, dc = self.directions[direction]
            next_row, next_col = row + dr, col + dc
            if not self.in_bounds(next_row, next_col):
                return 0
            state = (next_row, next_col, direction)
            if state in visited:
                return 0

            visited.add(state)
            cell = self.grid[next_row][next_col]

            if cell == ".":
                return dfs(next_row, next_col, direction)

            if cell == "^":
                return (
                    1
                    + dfs(next_row, next_col, "L")
                    + dfs(next_row, next_col, "R")
                )
            return 0
        return dfs(self.start_row, self.start_col, "D")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-part", type=int, required=True, help="1 ou 2")
  parser.add_argument("-test", type=str, required=True, help="True / False")
  args = parser.parse_args()

  test = args.test.lower() == "true"
  solution = Solution(test=test)

  if args.part == 1:
      print(solution.part1())
  else:
      print(solution.part2())
