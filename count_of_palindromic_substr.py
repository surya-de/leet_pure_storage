class Solution:
    def countSubstrings(self, s):
    	n = len(s)
    	_sum = 0
    	substrs = [[None for i in range(n)] for a in range(n)]
    	# Find substring of length-1
    	for x in range(0, n):
    		substrs[x][x] = 1
    		_sum += 1
    	# Find substrings of length-2
    	for x in range(0, n - 1):
    		if s[x] == s[x + 1]:
    			substrs[x][x + 1] = 1
    			_sum += 1

    	window_size = 3
    	while window_size <= n:
    		print(window_size)
    		strt = 0
    		itert = n - window_size + 1
    		print(window_size, itert)
    		while strt < itert:
    			end = strt + window_size -1
    			if s[strt] == s[end] and substrs[strt + 1][end - 1] == 1:
    				print('Updating for', strt, end)
    				substrs[strt][end] = 1
    				_sum += 1
    			strt += 1
    		window_size += 1
    	print(substrs)
if __name__ == '__main__':
	s = Solution()
	#inp = 'abc'
	inp = 'aaaaa'
	#inp = ''
	s.countSubstrings(inp)