#--coding=utf-8--

# 遍历二叉树的神级方法
# 【题目】
#     给定一棵二叉树的头节点 head，完成二叉树的先序、中序和后序遍历。如果二叉树的节点数为 N，
# 要求时间复杂度为 O(N)，额外空间复杂度为 O(1)。

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def morris_in(head):
	if not head:
		return
	cur1, cur2 = head, None
	while cur1:
		cur2 = cur1.left
		if cur2:
			while cur2.right and cur2.right != cur1:
				cur2 = cur2.right
			if not cur2.right:
				cur2.right = cur1
				cur1 = cur1.left
				continue
			else:
				cur2.right = None
		print cur1.value,
		cur1 = cur1.right
	print ''

def morris_pre(head):
	if not head:
		return
	cur1, cur2 = head, None
	while cur1:
		cur2 = cur1.left
		if cur2:
			while cur2.right and cur2.right != cur1:
				cur2 = cur2.right
			if not cur2.right:
				cur2.right = cur1
				print cur1.value,
				cur1 = cur1.left
				continue
			else:
				cur2.right = None
		else:
			print cur1.value,
		cur1 = cur1.right
	print ''

def morris_pos(head):
	if not head:
		return
	cur1, cur2 = head, None
	while cur1:
		cur2 = cur1.left
		if cur2:
			while cur2.right and cur2.right != cur1:
				cur2 = cur2.right
			if not cur2.right:
				cur2.right = cur1
				cur1 = cur1.left
				continue
			else:
				cur2.right = None
				print_edge(cur1.left)
		cur1 = cur1.right
	print_edge(head)
	print ''

def print_edge(head):
	tail = reverse_edge(head)
	cur = tail
	while cur:
		print cur.value,
		cur = cur.right
	reverse_edge(tail)

def reverse_edge(head):
	pre, next = None, None
	while head:
		next = head.right
		head.right = pre
		pre = head
		head = next
	return pre

def test():
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(4)
	node5 = Node(5)
	node6 = Node(6)
	node7 = Node(7)

	node1.left, node1.right = node2, node3
	node2.left = node4
	node4.right = node7
	node3.left, node3.right = node5, node6
	head = node1

#             1
#            / \
#           2   3
#          /   / \
#         4   5   6
#          \
#           7

	print 'morris_in:'
	morris_in(head)
	print 'morris_pre:'
	morris_pre(head)
	print 'morris_pos:'
	morris_pos(head)
	
if __name__ == '__main__':
	test()
