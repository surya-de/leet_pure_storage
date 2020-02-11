class Solution:
    def evalRPN(self, tokens):
    	def popElements(s):
    		b = int(s.pop())
    		a = int(s.pop())
    		return (a, b)
    	stack = []
    	operators = ['+', '-', '/', '*']
    	if len(tokens) == 0:
    		return 0
    	for token in tokens:
    		if token not in operators:
    			stack.append(token)
    		else:
    			f_st, s_nd = popElements(stack)
    			if token == '+':
    				new_entry = f_st + s_nd
    			elif token == '-':
    				new_entry = f_st - s_nd
    			elif token == '*':
    				new_entry = f_st * s_nd
    			else:
    				if s_nd == 0:
    					new_entry = 0
    				else:
    					new_entry = f_st / s_nd
    			stack.append(new_entry)
    	return(int(stack.pop()))
if __name__ == '__main__':
	s = Solution()
	#t = ["4", "13", "5", "/", "+"]
	#t = []
	#t = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
	t = ['0', '3', '/']
	print(s.evalRPN(t))