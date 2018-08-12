# https://leetcode.com/problems/number-of-islands/description/
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        no_of_islands = 0
        def mark_visited(grid, row, col):
            if row>=0 and row<len(grid) and col>=0 and col<len(grid[0]):
                if grid[row][col]=="1":
                    grid[row][col]="0"
                    mark_visited(grid, row+1, col)
                    mark_visited(grid, row-1, col)
                    mark_visited(grid, row, col+1)
                    mark_visited(grid, row, col-1)
                    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1":
                    no_of_islands+=1
                    mark_visited(grid, row, col)
                    
        return no_of_islands