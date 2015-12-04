#--coding=utf-8--

# 打印二叉树的边界节点
# 【题目】
#     给定一棵二叉树的头节点 head，按照如下两种标准分别实现二叉树边界节点的逆时针打印。
#     标准一：
#     1. 头节点为边界节点。
#     2. 叶节点为边界节点。
#     3. 如果节点在其所在的层中是最左或最右的，那么也是边界节点。
#     标准二：
#     1. 头节点为边界节点。
#     2. 叶节点为边界节点。
#     3. 树左边界延伸下去的路径为边界节点。
#     4. 树右边界延伸下去的路径为边界节点。
#     例如，如图所示的树。
#                                1
#                           ____/ \____
#                          /           \
#                         2             3
#                          \           / \
#                           4         5   6
#                          / \       / \
#                         7  8       9 10
#                             \     /
#                             11   12
#                            / \   / \
#                           13 14 15 16
#     按标准一的打印结果为： 1,2,4,7,11,13,14,15,16,12,10,6,3
#     按标准二的打印结果为： 1,2,4,7,13,14,15,16,10,6,3
# 【要求】
#     1. 如果节点数为 N，两种标准实现的时间复杂度要求都为 O(N)，额外空间复杂度要求都为 O(h)，h 为二叉树的高度。
#     2. 两种标准都要求逆时针顺序且不重复打印所有的边界节点。

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def print_edge1(head):
	if not head:
		return
	height = get_height(head, 0)
	edge_map = []
	for i in range(height):
		edge_map.append([None, None])
	set_edge_map(head, 0, edge_map)
	for i in range(height):
		print edge_map[i][0].value,
	print_leaf_not_in_map(head, 0, edge_map)
	for i in range(height - 1, -1, -1):
		if edge_map[i][0] != edge_map[i][1]:
			print edge_map[i][1].value,
	print ''

def get_height(h, l):
	if not h:
		return l
	return max(get_height(h.left, l + 1), get_height(h.right, l + 1))

def set_edge_map(h, l, edge_map):
	if not h:
		return
	edge_map[l][0] = edge_map[l][0] if edge_map[l][0] else h
	edge_map[l][1] = h
	set_edge_map(h.left, l + 1, edge_map)
	set_edge_map(h.right, l + 1, edge_map)

def print_leaf_not_in_map(h, l, m):
	if not h:
		return
	if not h.left and not h.right and h != m[l][0] and h != m[l][1]:
		print h.value,
	print_leaf_not_in_map(h.left, l + 1, m)
	print_leaf_not_in_map(h.right, l + 1, m)

def print_edge2(head):
	if not head:
		return
	print head.value,
	if head.left and head.right:
		print_left_edge(head.left, True)
		print_right_edge(head.right, True)
	else:
		print_edge2(head.left if head.left else head.right)
	print ''

def print_left_edge(h, p):
	if not h:
		return
	if p or (not h.left and not h.right):
		print h.value,
	print_left_edge(h.left, p)
	print_left_edge(h.right, p and (not h.left))

def print_right_edge(h, p):
	if not h:
		return
	print_right_edge(h.left, p and (not h.right))
	print_right_edge(h.right, p)
	if p or (not h.left and not h.right):
		print h.value,

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
	node10 = Node(10)
	node11 = Node(11)
	node12 = Node(12)
	node13 = Node(13)
	node14 = Node(14)
	node15 = Node(15)
	node16 = Node(16)

	node1.left, node1.right = node2, node3
	node2.right = node4
	node4.left, node4.right = node7, node8
	node8.right = node11
	node11.left, node11.right = node13, node14
	node3.left, node3.right = node5, node6
	node5.left, node5.right = node9, node10
	node9.left = node12
	node12.left, node12.right = node15, node16
	head = node1
	
	print 'print_edge1:',
	print_edge1(head)
	print 'print_edge2:',
	print_edge2(head)

if __name__ == '__main__':
	test()
