class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
    	row_flag = 0
    	col_flag = 0

    	# Check for the first element
    	if obstacleGrid[0][0] == 1:
    		row_flag = 1
    		col_flag = 1
    		obstacleGrid[0][0] = 0
    	else:
    		obstacleGrid[0][0] = 1

    	# Populate the first row
    	for row in range(1, len(obstacleGrid[0])):
    		if row_flag == 0:
    			if obstacleGrid[0][row] == 1:
    				obstacleGrid[0][row] = 0
    				row_flag = 1
    			else:
    				obstacleGrid[0][row] = 1
    		else:
    			obstacleGrid[0][row] = 0

    	# Populate the first column
    	for col in range(1, len(obstacleGrid)):
    		if col_flag == 0:
    			if obstacleGrid[col][0] == 1:
    				obstacleGrid[col][0] = 0
    				col_flag = 1
    			else:
    				obstacleGrid[col][0] = 1
    		else:
    			obstacleGrid[col][0] = 0

    	# Populate the center pieces
    	for rows in range(1, len(obstacleGrid)):
    		for cols in range(1, len(obstacleGrid[0])):
    			if obstacleGrid[rows][cols] != 1:
    				obstacleGrid[rows][cols] = obstacleGrid[rows][cols - 1] + obstacleGrid[rows - 1][cols]
    			else:
    				obstacleGrid[rows][cols] = 0

    	return obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]

if __name__ == '__main__':
	inp = [
			[0,0,0],
  			[0,1,0],
  			[0,0,0]
		]

	s = Solution()
	print(s.uniquePathsWithObstacles(inp))