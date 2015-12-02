#--coding=utf-8--

# 分别用递归和非递归方式实现二叉树先序、中序和后序遍历
# 【题目】
#     用递归和非递归方式，分别按照二叉树先序、中序和后序打印所有的节点。
#     我们约定：先序遍历顺序为根、左、右；中序遍历顺序为左、根、右；后序遍历顺序为左、右、根。

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def pre_order_recur(head):
	if not head:
		return
	print head.value,
	pre_order_recur(head.left)
	pre_order_recur(head.right)

def in_order_recur(head):
	if not head:
		return
	in_order_recur(head.left)
	print head.value,
	in_order_recur(head.right)

def pos_order_recur(head):
	if not head:
		return
	pos_order_recur(head.left)
	pos_order_recur(head.right)
	print head.value,

def pre_order_unrecur(head):
	if not head:
		return
	stack = []
	stack.append(head)
	while len(stack):
		cur = stack.pop()
		print cur.value,
		if cur.right:
			stack.append(cur.right)
		if cur.left:
			stack.append(cur.left)

def in_order_unrecur(head):
	if not head:
		return
	stack = []
	while len(stack) or head:
		if head:
			stack.append(head)
			head = head.left
		else:
			head = stack.pop()
			print head.value,
			head = head.right

def pos_order_unrecur(head):
	if not head:
		return
	stack1, stack2 = [], []
	stack1.append(head)
	while len(stack1):
		head = stack1.pop()
		stack2.append(head)
		if head.left:
			stack1.append(head.left)
		if head.right:
			stack1.append(head.right)
	while len(stack2):
		print stack2.pop().value,

def pos_order_unrecur2(head):
	if not head:
		return
	stack = []
	stack.append(head)
	c = None
	while len(stack):
		c = stack[-1]
		if c.left and head != c.left and head != c.right:
			stack.append(c.left)
		elif c.right and head != c.right:
			stack.append(c.right)
		else:
			print stack.pop().value,
			head = c

def test():
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(4)
	node5 = Node(5)
	node6 = Node(6)
	node7 = Node(7)
	node8 = Node(8)
	node9 = Node(9)

	node6.left, node6.right = node4, node7
	node4.left, node4.right = node2, node5
	node7.right = node9
	node2.left, node2.right = node1, node3
	node9.left = node8
	head = node6

#             6
#            / \
#           4   7
#          / \   \
#         2   5   9
#        / \     /
#       1   3   8
	
	print 'pre_order_recur:',
	pre_order_recur(head)
	print ''
	print 'in_order_recur:',
	in_order_recur(head)
	print ''
	print 'pos_order_recur:',
	pos_order_recur(head)
	print ''
	print '==================================='
	print 'pre_order_unrecur:',
	pre_order_unrecur(head)
	print ''
	print 'in_order_unrecur:',
	in_order_unrecur(head)
	print ''
	print 'pos_order_unrecur:',
	pos_order_unrecur(head)
	print ''
	print 'pos_order_unrecur2:',
	pos_order_unrecur2(head)
	print ''

if __name__ == '__main__':
	test()
