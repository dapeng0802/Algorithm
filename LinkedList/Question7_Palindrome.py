#--coding=utf-8--

# 判断一个链表是否为回文结构
# 【题目】
#     给定一个链表的头节点 head，请判断该链表是否为回文结构。
#     例如：
#     1->2->1，返回 true。
#     1->2->2->1，返回 true。
#     15->6->15，返回 true。
#     1->2-31，返回 false。
#     进阶：
#     如果链表长度为 N，时间复杂度达到 O(N)，额外空间复杂度达到 O(1)。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def is_palindrome(head):
	stack = []
	cur = head
	while cur:
		stack.append(cur)
		cur = cur.next
	while head:
		if head.value != stack.pop().value:
			return False
		head = head.next
	return True

def is_palindrome2(head):
	if not head or not head.next:
		return True
	right = head.next
	cur = head
	while cur.next and cur.next.next:
		right = right.next
		cur = cur.next.next
	stack = []
	while right:
		stack.append(right)
		right = right.next
	while len(stack):
		if head.value != stack.pop().value:
			return False
		head = head.next
	return True

def is_palindrome3(head):
	if not head or not head.next:
		return True
	n1, n2 = head, head
	while n2.next and n2.next.next:
		n1 = n1.next
		n2 = n2.next.next
	n2 = n1.next
	n1.next = None
	n3 = None
	while n2:
		n3 = n2.next
		n2.next = n1
		n1 = n2
		n2 = n3
	n3 = n1
	n2 = head
	res = True
	while n1 and n2:
		if n1.value != n2.value:
			res = False
			break
		n1 = n1.next
		n2 = n2.next
	n1 = n3.next
	n3.next = None
	while n1:
		n2 = n1.next
		n1.next = n3
		n3 = n1
		n1 = n2
	return res

def show_list(head):
	cur = head.next
	print head.value,
	while cur:
		print '->', cur.value,
		cur = cur.next
	print ''

def test():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(2)
	head.next.next.next = Node(1)
	show_list(head)
	print 'is_palindrome:', is_palindrome3(head)

if __name__ == '__main__':
	test()
