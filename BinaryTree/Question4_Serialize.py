#--coding=utf-8--

# 二叉树的序列化和反序列化
# 【题目】
#     二叉树被记录成文件的过程叫作二叉树的序列化，通过文件内容重建原来二叉树的过程叫作二叉树的反序列化。
# 给定一棵二叉树的头节点 head，并已知二叉树节点值的类型为 32 位整型。请设计一种二叉树序列化和反序列化
# 的方案，并用代码实现。

from collections import deque

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

def serial_by_level(head):
	if not head:
		return '#!'
	res = str(head.value) + '!'
	queue = deque()
	queue.append(head)
	while len(queue):
		head = queue.popleft()
		if head.left:
			res += str(head.left.value) + '!'
			queue.append(head.left)
		else:
			res += '#!'
		if head.right:
			res += str(head.right.value) + '!'
			queue.append(head.right)
		else:
			res += '#!'
	return res

def recon_by_level_string(level_str):
	values = level_str.split('!')
	index = 0
	head = generate_node_by_string(values[index])
	index += 1
	queue = deque()
	if head:
		queue.append(head)
	node = None
	while len(queue):
		node = queue.popleft()
		node.left = generate_node_by_string(values[index])
		index += 1
		node.right = generate_node_by_string(values[index])
		index += 1
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	return head

def generate_node_by_string(val):
	if val == '#':
		return None
	return Node(int(val))

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
	print 'serialize_by_pre:', str_tree
	from Question3_PrintTree import print_tree
	print 'recon_by_pre_string:'
	print_tree(recon_by_pre_string(str_tree))
	str_tree = serial_by_level(head)
	print 'serialize_by_level:', str_tree
	print 'recon_by_level_string:'
	print_tree(recon_by_level_string(str_tree))

if __name__ == '__main__':
	test()
