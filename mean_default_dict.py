import statistics
from collections import defaultdict
def trial(a):
	storage = defaultdict(list)
	final = []
	for i in range(0, len(a)):
		_mean = statistics.mean(a[i])
		storage[_mean].append(i)
	for key in storage.keys():
		final.append(storage[key])
	print(final)

if __name__ == '__main__':
	a = [[3,3,4,2], [4,4], [4,0,3,3], [2,3], [3,3,3]]
	trial(a)