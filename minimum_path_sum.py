class Solution:
    def minPathSum(self, grid):
    	# Populate the rows.
    	for i in range(1, len(grid[0])):
    		grid[0][i] = grid[0][i - 1] + grid[0][i]
    	# Populate the columns.
    	for j in range(1, len(grid)):
    		grid[j][0] = grid[j - 1][0] + grid[j][0]
    	# Populate the middle grids.
    	for rows in range(1, len(grid)):
    		for cols in range(1, len(grid[0])):
    			grid[rows][cols] = grid[rows][cols] + min(grid[rows - 1][cols], grid[rows][cols - 1])
    	print(grid)
if __name__ == '__main__':
	s = Solution()
	#inp = [[1,3,1], [1,5,1], [4,2,1]]
	inp = [[1,2,5],[3,2,1]]
	s.minPathSum(inp)