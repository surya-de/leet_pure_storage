class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def formList(self, l):
		tracker = ListNode(None)
		dummy = tracker
		for elems in l:
			tracker.next = ListNode(elems)
			tracker = tracker.next
		#self.printList(dummy.next)
		self.removeElements(dummy.next, 6)
	def printList(self, llist):
		while llist.next != None:
			print(llist.val, end = '->')
			llist = llist.next
		print(llist.val)
	def removeElements(self, head, val):
		dum = ListNode(None)
		track = dum
		try:
			while head.next != None:
				if head.val == val:
					head = head.next
				else:
					dum.next = head
					dum = dum.next
					head = head.next
			if head.val == val:
				head = head.next
				dum.next = head
			else:
				dum.next = head
			return track.next

		except AttributeError:
			return 1

if __name__ == '__main__':
	#lis = [1,2,6,3,4,5,6]
	#lis = [1]
	lis = []
	s = Solution()
	print(s.formList(lis))