class Solution(object):
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        def findMaxArea(grid, row, col):
            if row>=0 and row<len(grid) and col>=0 and col<len(grid[0]):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    return 1 + findMaxArea(grid, row+1, col) + findMaxArea(grid, row-1, col) + findMaxArea(grid, row, col+1) + findMaxArea(grid, row, col-1)
            return 0
    
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    area = findMaxArea(grid, row, col)
                    maxArea = max(area, maxArea)
        return maxArea

if __name__ == '__main__':
    s = Solution()
    print s.maxAreaOfIsland([[1]])