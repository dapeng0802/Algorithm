#--coding=utf-8--

# 将单链表的每 K 个节点之间逆序
# 【题目】
#     给定一个单链表的头节点 head，实现一个调整单链表的函数，使得每 K 个节点之间逆序，
# 如果最后不够 K 个节点一组，则不调整最后几个节点。
#     例如：
#     链表：1->2->3->4->5->6->7->8->null，K=3。
#     调整后为：3->2->1->6->5->4->7->8->null。其中 7、8 不调整，因为不够一组。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(self.value, cmpres.value), 0)

def reverse_k_nodes(head, K):
	if not head or K < 2:
		return head
	count = K
	stack = []
	result = Node(0)
	tmp = result
	while head:
		count -= 1
		stack.append(head)
		head = head.next
		if count == 0:
			while len(stack):
				tmp.next = stack.pop()
				tmp = tmp.next
			count = K
	if count:
		next, cur = None, None
		while len(stack):
			cur = stack.pop()
			cur.next = next
			next = cur
		tmp.next = next
	return result.next

def reverse_k_nodes2(head, K):
	if not head or K < 2:
		return head
	count = K
	result = None
	new_head, new_tail, old_tail = None, None, None
	next, pre = None, None
	while head:
		count -= 1
		next = head.next
		head.next = pre
		pre = head
		head = next
		if not new_tail:
			new_tail = pre
		if count == 0:
			new_head = pre
			result = new_head if not result else result
			if old_tail:
				old_tail.next = new_head
			old_tail = new_tail
			new_tail = None
			next, pre = None, None
			count = K
	if count:
		old_tail.next = reverse_list(pre)
	
	return result

def reverse_list(head):
	if not head:
		return head
	next, pre = None, None
	while head:
		next = head.next
		head.next = pre
		pre = head
		head = next
	return pre

def show_list(head):
	if not head:
		return
	cur = head.next
	print head.value,
	while cur:
		print '->', cur.value,
		cur = cur.next
	print '-> None'

def test():
	nodes = [Node(1), Node(3), Node(5), Node(7), Node(9), Node(11), Node(13)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head = nodes[0]
	
	print 'head:',
	show_list(head)
	print 'reverse_k_nodes:',
	show_list(reverse_k_nodes2(head, 4))

if __name__ == '__main__':
	test()
