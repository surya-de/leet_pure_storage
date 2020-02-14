class Solution:
    def sortColors(self, nums):
    	lo = 0
    	reader = 0
    	hi = len(nums) - 1

    	while reader <= hi:
    		if nums[reader] == 0:
    			# Swap the low and reader values.
    			nums[reader], nums[lo] = nums[lo], nums[reader]
    			# Increment the reader and lo pointers.
    			lo += 1
    			reader += 1
    		elif nums[reader] == 1:
    			reader += 1
    		else:
    			nums[reader], nums[hi] = nums[hi], nums[reader]
    			hi -= 1
    	print(nums)

if __name__ == '__main__':
	s = Solution()
	#seris = [2, 0, 2, 1, 1, 0]
	seris = [0, 1, 2, 0]
	s.sortColors(seris)
        