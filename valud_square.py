import math
from collections import Counter
class Solution:
    def validSquare(self, p1, p2, p3, p4):
    	distance = []
    	def find_distance(x, y):
    		return math.sqrt(((x[1] - y[1]) ** 2) + ((x[0] - y[0]) ** 2))
    	
    	p1p2 = find_distance(p1, p2)
    	distance.append(p1p2)
    	p1p3 = find_distance(p1, p3)
    	distance.append(p1p3)
    	p1p4 = find_distance(p1, p4)
    	distance.append(p1p4)
    	p2p3 = find_distance(p2, p3)
    	distance.append(p2p3)
    	p2p4 = find_distance(p2, p4)
    	distance.append(p2p4)
    	p3p4 = find_distance(p3, p4)
    	distance.append(p3p4)
    	cnt = list(Counter(distance).values())
    	if cnt == [2, 4] or cnt == [4, 2]:
    		return True
    	return False

if __name__ == '__main__':
	s = Solution()
	p1 = [0, 0]
	p2 = [0, 0]
	p3 = [0, 0]
	p4 = [0, 0]
	print(s.validSquare(p1, p2, p3, p4))
        