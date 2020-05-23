'''
	@author: Suryadeep
'''
class Solution:
	def uniquePaths(self, m, n):
		# Create a storage matrix
		store = [[1] * n for _ in range(m)]
		for cols in range(1, m):
			for rows in range(1, n):
				store[cols][rows] = store[cols][rows  - 1] + store[cols - 1][rows]
		print(store[m - 1][n - 1])

if __name__ == '__main__':
	s = Solution()
	s.uniquePaths(7, 3)