#--coding=utf-8--

# 如何较为直观地打印二叉树
# 【题目】
#     二叉树可以用常规的三种遍历结果来描述其结构，但是不够直观，尤其是二叉树中有重复值的时候，
# 仅通过三种遍历的结果来构造二叉树的真实结构更是难上加难，有时则根本不可能。给定一棵二叉树的头
# 节点 head，已知二叉树节点值的类型为 32 位整型，请实现一个打印二叉树的函数，可以直观地展示
# 树的形状，也便于画出真实的结构。

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def print_tree(head):
	print 'Binary Tree:'
	print_inorder(head, 0, 'H', 17)
	print ''

def print_inorder(head, height, to, length):
	if not head:
		return
	print_inorder(head.right, height + 1, 'v', length)
	val = to + str(head.value) + to
	lenM = len(val)
	lenL = (length - lenM) / 2
	lenR = length -lenM - lenL
	val = get_space(lenL) + val + get_space(lenR)
	print get_space(height * length) + val
	print_inorder(head.left, height + 1, '^', length)

def get_space(num):
	space = ' '
	str_list = []
	for i in xrange(num):
		str_list.append(space)
	return ''.join(str_list)

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

	print_tree(head)

if __name__ == '__main__':
	test()
