#--coding=utf-8--

# 二叉树的序列化和反序列化
# 【题目】
#     二叉树被记录成文件的过程叫作二叉树的序列化，通过文件内容重建原来二叉树的过程叫作二叉树的反序列化。
# 给定一棵二叉树的头节点 head，并已知二叉树节点值的类型为 32 位整型。请设计一种二叉树序列化和反序列化
# 的方案，并用代码实现。

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def serial_by_pre(head):
	if not head:
		return '#!'
	res = str(head.value) + '!'
	res += serial_by_pre(head.left)
	res += serial_by_pre(head.right)
	return res

def recon_by_pre_string(pre_str):
	values = pre_str.split('!')
	from collections import deque
	queue = deque()
	for i in xrange(len(values)):
		queue.append(values[i])
	return recon_pre_order(queue)

def recon_pre_order(queue):
	value = queue.popleft()
	if value == '#':
		return None
	head = Node(int(value))
	head.left = recon_pre_order(queue)
	head.right = recon_pre_order(queue)
	return head

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

	str_tree = serial_by_pre(head)
	print 'serialize:', str_tree
	from Question3_PrintTree import print_tree
	print_tree(recon_by_pre_string(str_tree))

if __name__ == '__main__':
	test()
