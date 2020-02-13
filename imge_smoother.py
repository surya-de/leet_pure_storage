class Solution:
    def imageSmoother(self, M):
    	coors = []
    	cntr = 0
    	summ = 0
    	len_row = len(M)
    	len_col = len(M[0])
    	trav_coordinates = [(-1, -1), (-1, 0), (-1, 1),
    						(0, -1), (0, 0), (0, 1),
    						(1, -1), (1, 0), (1, 1)]
    	Op = [[0 for a in range(len_col)] for b in range(len_row)]
    	for rows in range(len(M)):
    		for cols in range(len(M[0])):
    			cntr = 0
    			summ = 0
    			for x, y in trav_coordinates:
    				loc_x = rows + x
    				loc_y = cols + y
    				if loc_x > -1 and loc_y > -1 and loc_x < len_row and loc_y < len_col:
    					summ += M[loc_x][loc_y]
    					cntr += 1
    			Op[rows][cols] = summ // cntr
    	return Op
if __name__ == '__main__':
	#ls = [[1,1,1], [1,0,1], [1,1,1]]
	ls = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
	s = Solution()
	print(s.imageSmoother(ls))