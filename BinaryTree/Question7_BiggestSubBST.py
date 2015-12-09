#--coding=utf-8--

# 找到二叉树中的最大搜索二叉子树
# 【题目】
#     给定一棵二叉树的头节点 head，已知其中所有节点的值都不一样，找到含有节点最多的搜索二叉子树，并返回这棵子树的头节点。
#     例如，二叉树如下图所示。
#                            6
#                          /   \
#                         1     12
#                        / \   /   \
#                       0   3 10    13
#                            /  \   / \
#                           4   14 20 16
#                          / \  / \
#                         2  5 11 15
#     这棵树中的最大搜索二叉子树如下图所示。
#                             10
#                            /  \
#                           4   14
#                          / \  / \
#                         2  5 11 15
# 【要求】
#     如果节点数为 N，要求时间复杂度为 O(N)，额外空间复杂度为 O(h)，h 为二叉树的高度。

import sys

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def biggest_sub_BST(head):
	record = [0, 0, 0]
	return pos_order(head, record)

def pos_order(head, record):
	if not head:
		record[0] = 0
		record[1] = sys.maxint
		record[2] = -sys.maxint
		return None
	value = head.value
	left, right = head.left, head.right
	l_BST = pos_order(left, record)
	l_size, l_min, l_max = record[0], record[1], record[2]
	r_BST = pos_order(right, record)
	r_size, r_min, r_max = record[0], record[1], record[2]
	record[1] = min(l_min, value)
	record[2] = max(r_max, value)
	if left == l_BST and right == r_BST and l_max < value and value < r_min:
		record[0] = l_size + r_size + 1
		return head
	record[0] = max(l_size, r_size)
	return l_BST if l_size > r_size else r_BST

def test():
	node1 = Node(6)
	node2 = Node(1)
	node3 = Node(12)
	node4 = Node(0)
	node5 = Node(3)
	node6 = Node(10)
	node7 = Node(13)
	node8 = Node(4)
	node9 = Node(14)
	node10 = Node(20)
	node11 = Node(16)
	node12 = Node(2)
	node13 = Node(5)
	node14 = Node(11)
	node15 = Node(15)

	node1.left, node1.right = node2, node3
	node2.left, node2.right = node4, node5
	node3.left, node3.right = node6, node7
	node6.left, node6.right = node8, node9
	node7.left, node7.right = node10, node11
	node8.left, node8.right = node12, node13
	node9.left, node9.right = node14, node15
	head = node1

#                            6
#                          /   \
#                         1     12
#                        / \   /   \
#                       0   3 10    13
#                            /  \   / \
#                           4   14 20 16
#                          / \  / \
#                         2  5 11 15

	print biggest_sub_BST(head).value

if __name__ == '__main__':
	test()
