#--coding=utf-8--

# 构造数组的 MaxTree
# 【题目】
#     定义二叉树节点如下：
#         public class Node {
#             public int value;
#             public Node left;
#             public Node right;
#             public Node(int data) {
#                 this.value = data
#             }
#         }
#
#     一个数组的 MaxTree 定义如下：
#     1. 数组必须没有重复元素。
#     2. MaxTree 是一棵二叉树，数组的每一个值对应一个二叉树节点。
#     3. 包括 MaxTree 树在内且在其中的每一棵子树上，值最大的节点都是树的头。
#     给定一个没有重复元素的数组 arr，写出生成这个数组的 MaxTree 的函数，要求如果数组长度为 N，则时间复杂度为 O(N)、额外空间复杂度为 O(N)。

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

def getMaxTree(arr):
	node_arr = []
	for i in range(len(arr)):
		node_arr.append(Node(arr[i]))
	stack = []
	lBigDic = {}
	rBigDic = {}
	for i in range(len(node_arr)):
		curNode = node_arr[i]
		while len(stack) > 0 and stack[-1].value < curNode.value:
			popStackSetDic(stack, lBigDic)
		stack.append(curNode)
	while len(stack) > 0:
		popStackSetDic(stack, lBigDic)
	for i in range(len(node_arr))[::-1]:
		curNode = node_arr[i]
		while len(stack) > 0 and stack[-1].value < curNode.value:
			popStackSetDic(stack, rBigDic)
		stack.append(curNode)
	while len(stack) > 0:
		popStackSetDic(stack, rBigDic)
	head = None
	for i in range(len(node_arr)):
		curNode = node_arr[i]
		left = lBigDic.get(curNode)
		right = rBigDic.get(curNode)
		if left == None and right == None:
			head = curNode
		elif left == None:
			if right.left == None:
				right.left = curNode
			else:
				right.right = curNode
		elif right == None:
			if left.left == None:
				left.left = curNode
			else:
				left.right = curNode
		else:
			parent = left if left.value < right.value else right
			if parent.left == None:
				parent.left = curNode
			else:
				parent.right = curNode
	return head

def popStackSetDic(stack, dic):
	popNode = stack.pop()
	if len(stack) == 0:
		dic.setdefault(popNode, None)
	else:
		dic.setdefault(popNode, stack[-1])

def showTree(node):
	if node == None:
		return
	print '(',
	print node.value,
	showTree(node.left)
	showTree(node.right)
	print ')',

def test():
	arr = [3, 4, 5, 1, 2]
	max_tree = getMaxTree(arr)
	showTree(max_tree)

if __name__ == '__main__':
	test()
