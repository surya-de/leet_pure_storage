class Solution:
    def twoSum(self, numbers, target):
    	op = []
    	lo = 0
    	hi = len(numbers) - 1
    	while lo < hi:
    		summ = numbers[lo] + numbers[hi]
    		if summ > target:
    			hi -= 1
    		elif summ < target:
    			lo += 1
    		else:
    			op.append(lo + 1)
    			op.append(hi + 1)
    			return op
    	else:
    		op.append(-1)
    		op.append(-1)
    		return op


if __name__ == '__main__':
	s = Solution()
	#numbers = [2,7,11,15]
	numbers = [2, 4, 5]
	target = 10
	print(s.twoSum(numbers, target))