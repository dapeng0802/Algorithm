#--coding=utf-8--

# 反转单向和双向链表
# 【题目】
#     分别实现反转单向链表和反转双向链表的函数。
# 【要求】
#     如果链表的长度为 N，事件复杂度要求为 O(N)，额外空间复杂度要求为 O(1)。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def reverse_list(head):
	pre, next = None, None
	while head:
		next = head.next
		head.next = pre
		pre = head
		head = next
	return pre
	
class DoubleNode(object):
	last = None
	next = None
	def __init__(self, data):
		self.value = data

def reverse_double_list(head):
	pre, next = None, None

	while head:
		next = head.next
		head.next = pre
		head.last = next
		pre = head
		head = next
	return pre

def test():
	head = Node(0)
	cur = head
	for i in range(1, 20):
		cur.next = Node(i)
		cur = cur.next
	head = reverse_list(head)
	cur = head
	while cur:
		print cur.value, '->',
		cur = cur.next
	print ''

def test_double():
	head = DoubleNode(0)
	cur = head
	for i in range(1, 20):
		cur.next = DoubleNode(i)
		cur = cur.next
	cur = head
	while cur and cur.next:
		cur.next.last = cur
		cur = cur.next
	head = reverse_double_list(head)
	cur = head
	while cur:
		print 'cur:', cur.value, 'cur->last:', cur.last.value if cur.last else None,\
		'cur->next:', cur.next.value if cur.next else None
		cur = cur.next


if __name__ == '__main__':
	test()
	test_double()