#--coding=utf-8--

# 在单链表和双链表中删除倒数第 K 个节点
# 【题目】
#     分别实现两个函数，一个可以删除单链表中倒数第 K 个节点，另一个可以删除双联表中倒数第 K 个节点。
# 【要求】
#     如果链表长度为 N，时间复杂度达到 O(N)，额外空间复杂度达到 O(1)。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def remove_last_kth_node(head, last_kth):
	if head == None or last_kth < 0:
		return head
	cur = head
	while cur:
		last_kth -= 1
		cur = cur.next
	if last_kth == 0:
		head = head.next
	if last_kth < 0:
		cur = head
		while last_kth != 0:
			last_kth += 1
			if last_kth == 0:
				break
			cur = cur.next
		cur.next = cur.next.next
	return head

def test():
	head = Node(0)
	cur = head
	for i in range(1, 20):
		cur.next = Node(i)
		cur = cur.next
	head = remove_last_kth_node(head, 5)
	cur = head
	while cur:
		print cur.value, '->',
		cur = cur.next
	print ''

class DoubleNode(object):
	last = None
	next = None
	def __init__(self, data):
		self.value = data

def remove_last_kth_node_double(head, last_kth):
	if head == None or last_kth < 0:
		return head
	cur = head
	while cur != None:
		last_kth -= 1
		cur = cur.next
	if last_kth == 0:
		head = head.next
		head.last = None
	if last_kth < 0:
		cur = head
		while last_kth != 0:
			last_kth += 1
			if last_kth == 0:
				break
			cur = cur.next
		cur.next = cur.next.next
		if cur.next:
			cur.next.last = cur
	return head

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
	head = remove_last_kth_node_double(head, 5)
	cur = head
	while cur:
		print 'cur:', cur.value, 'cur->last:', cur.last.value if cur.last else None,\
		'cur->next:', cur.next.value if cur.next else None
		cur = cur.next

if __name__ == '__main__':
	test()
	test_double()