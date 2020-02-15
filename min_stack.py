class MinStack:
	def __init__(self):
		self.stack = list()

	# Module to push to stack.
	def push(self, x):
		self.stack.append(x)
	
	# Module to pop from stack.
	def pop(self):
		self.stack.pop()

	# Module to find top.
	def top(self):
		return self.stack[-1]

	# Module to find the minimum.
	def getMin(self):
		return min(self.stack)
        

if __name__ == '__main__':
	mnStack = MinStack()
	mnStack.push(-2)
	mnStack.push(0)
	mnStack.push(-3)
	print(mnStack.stack)
	print(mnStack.getMin())
	mnStack.pop()
	print(mnStack.stack)
	print(mnStack.top())
	print(mnStack.getMin())