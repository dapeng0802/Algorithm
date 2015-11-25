#--coding=utf-8--

# 两个单链表相交的一系列问题
# 【题目】
#     在本题中，单链表可能有环，也可能无环。给定两个单链表的头节点 head1 和 head2，这两个链表可能相交，
# 也可能不相交。请实现一个函数，如果两个链表相交，请返回相交的第一个节点；如果不相交，返回 null 即可。
# 【要求】
#     如果链表 1 的长度为 N，链表 2 的长度为 M，时间复杂度请达到 O(N+M)，额外空间复杂度请达到 O(1)。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(self.value, cmpres.value), 0)

def get_loop_node(head):
	if not head or not head.next or not head.next.next:
		return None
	n1 = head.next
	n2 = head.next.next
	while n1 != n2:
		if not n2.next or not n2.next.next:
			return None
		n2 = n2.next.next
		n1 = n1.next
	n2 = head
	while n1 != n2:
		n1 = n1.next
		n2 = n2.next
	return n1

def no_loop(head1, head2):
	if not head1 or not head2:
		return None
	cur1, cur2 = head1, head2
	n = 0
	while cur1.next:
		n += 1
		cur1 = cur1.next
	while cur2.next:
		n -= 1
		cur2 = cur2.next
	if cur1 != cur2:
		return None
	cur1 = head1 if n > 0 else head2
	cur2 = head2 if cur1 == head1 else head1
	n = abs(n)
	while n:
		n -= 1
		cur1 = cur1.next
	while cur1 != cur2:
		cur1 = cur1.next
		cur2 = cur2.next
	print cur1 == cur2
	return cur1

def both_loop(head1, loop1, head2, loop2):
	cur1, cur2 = None, None
	if loop1 == loop2:
		cur1, cur2 = head1, head2
		n = 0
		while cur1 != loop1:
			n += 1
			cur1 = cur1.next
		while cur2 != loop2:
			n -= 1
			cur2 = cur2.next
		cur1 = head1 if n > 0 else head2
		cur2 = head2 if cur1 == head1 else head2
		n = abs(n)
		while n:
			n -= 1
			cur1 = cur1.next
		while cur1 != cur2:
			cur1 = cur1.next
			cur2 = cur2.next
		return cur1
	else:
		cur1 = loop1.next
		while cur1 != loop1:
			if cur1 == loop2:
				return loop1
			cur1 = cur1.next
		return None

def get_intersect_node(head1, head2):
	if not head1 or not head2:
		return None
	loop1 = get_loop_node(head1)
	loop2 = get_loop_node(head2)
	if not loop1 and not loop2:
		return no_loop(head1, head2)
	if loop1 and loop2:
		return both_loop(head1, loop1, head2, loop2)
	return None

def show_list(head):
	if not head:
		return
	cur = head.next
	print head.value,
	while cur:
		print '->', cur.value,
		cur = cur.next
	print ''

def test():
	nodes = [Node(1), Node(3), Node(5), Node(7), Node(8), Node(9)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head1 = nodes[0]
	nodes = [Node(2), Node(4), Node(6), Node(7), Node(8), Node(9)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head2 = nodes[0]
	
	print 'head1:',
	show_list(head1)
	print 'head2:',
	show_list(head2)
	print 'get_intersect_node:',
	show_list(get_intersect_node(head1, head2))

if __name__ == '__main__':
	test()
