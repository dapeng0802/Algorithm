#--coding=utf-8--

# 在二叉树中找到累加和为指定值的最长路径长度
# 【题目】
#     给定一棵二叉树的头节点 head 和一个 32 位整数 sum，二叉树节点值类型为整型，求累加和为 sum 的最长路径长度。
# 路径是指从某个节点往下，每次最多选择一个孩子节点或者不选所形成的节点链。
#     例如，二叉树如图所示。
#               -3
#              /  \
#             3   -9
#            / \  / \
#           1  0 2   1
#             / \
#            1   6
#     如果 sum=6，那么累加和为 6 的最长路径为：-3,3,0,6，所以返回 4。
#     如果 sum=-9，那么累加和为 -9 的最长路径为：-9，所以返回 1。
#     注：本题不用考虑节点值相交可能溢出的情况。

from collections import deque

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def get_max_length(head, summy):
	dic = dict()
	dic[0] = 0
	return pre_order(head, summy, 0, 1, 0, dic)

def pre_order(head, summy, pre_sum, level, max_len, dic):
	if not head:
		return max_len
	cur_sum = pre_sum + head.value
	if not dic.has_key(cur_sum):
		dic[cur_sum] = level
	if dic.has_key(cur_sum - summy):
		max_len = max(level - dic.get(cur_sum - summy), max_len)
	max_len = pre_order(head.left, summy, cur_sum, level + 1, max_len, dic)
	max_len = pre_order(head.right, summy, cur_sum, level + 1, max_len, dic)
	if level == dic.get(cur_sum):
		dic.pop(cur_sum)
	return max_len

def test():
	node1 = Node(-3)
	node2 = Node(3)
	node3 = Node(-9)
	node4 = Node(1)
	node5 = Node(0)
	node6 = Node(2)
	node7 = Node(1)
	node8 = Node(1)
	node9 = Node(6)

	node1.left, node1.right = node2, node3
	node2.left, node2.right = node4, node5
	node3.left, node3.right = node6, node7
	node5.left, node5.right = node8, node9
	head = node1

#               -3
#              /  \
#             3   -9
#            / \  / \
#           1  0 2   1
#             / \
#            1   6

	print get_max_length(head, -9)
	print get_max_length(head, 6)

if __name__ == '__main__':
	test()
