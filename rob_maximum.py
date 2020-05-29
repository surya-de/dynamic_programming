class Solution:
    def rob(self, nums):
    	if len(nums) == 0:
    		return 0
    	if len(nums) == 1:
    		return nums[0]

    	nums[1] = max(nums[0], nums[1])
    	for i in range(2, len(nums)):
    		nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
    	return max(nums)
if __name__ == '__main__':
	inp = [1, 2, 3, 1]
	s = Solution()
	print(s.rob(inp))