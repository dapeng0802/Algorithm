#--coding=utf-8--

# 将搜索二叉树转换成双向链表
# 【题目】
#     对二叉树的节点来说，有本身的值域，有指向左孩子和右孩子的两个指针；对双向链表的节点来说，有本身的值域，
# 有指向上一个节点和下一个节点的指针。在结构上，两种结构有相似性，现在有一棵搜索二叉树，请将其转换为一个有序
# 的双向链表。
#     例如，节点定义为：
#     public class Node {
#         public int value;
#         public Node left;
#         public Node right;
#         public Node(int data) {
#             this.value = data;
#         }
#     }
#     一棵搜索二叉树如图所示：
#             6
#            / \
#           4   7
#          / \   \
#         2   5   9
#        / \     /
#       1   3   8
#     这棵搜索二叉树转换后的双向链表从头到尾依次是 1~9。对每一个节点来说，原来的 right 指针等价于转换后的 
# next 指针，原来的 left 指针等价于转换后的 last 指针，最后返回转换后的双向链表头节点。

from collections import deque

class Node(object):
	left, right = None, None
	def __init__(self, data):
		self.value = data

def convert(head):
	queue = deque()
	in_order_to_queue(head, queue)
	if len(queue) == 0:
		return head
	head = queue.popleft()
	pre = head
	pre.left = None
	cur = None
	while len(queue):
		cur = queue.popleft()
		pre.right = cur
		cur.left = pre
		pre = cur
	pre.right = None
	return head

def in_order_to_queue(head, queue):
	if not head:
		return
	in_order_to_queue(head.left, queue)
	queue.append(head)
	in_order_to_queue(head.right, queue)

def convert2(head):
	if not head:
		return None
	last = process(head)
	head = last.right
	last.right = None
	return head

def process(head):
	if not head:
		return None
	leftE = process(head.left)
	rightE = process(head.right)
	leftS = leftE.right if leftE else None
	rightS = rightE.right if rightE else None
	if leftE and rightE:
		leftE.right = head
		head.right = rightS
		rightS.left = head
		rightE.right = leftS
		return rightE
	elif leftE:
		leftE.right = head
		head.left = leftE
		head.right = leftS
		return head
	elif rightE:
		head.right = rightS
		rightS.left = head
		rightE.right = head
		return rightE
	else:
		head.right = head
		return head
	
def show_list(head):
	cur = head
	while cur:
		print 'cur:', cur.value, 'cur->left:', cur.left.value if cur.left else None,\
		'cur->right:', cur.right.value if cur.right else None
		cur = cur.right

def show_tree(head):
	if not head:
		print 'None',
		return
	print head.value, '(', 'left:',
	show_tree(head.left)
	print 'right:',
	show_tree(head.right)
	print ')',

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
	
	print 'head:'
	show_tree(node6)
	print ''
	print 'convert:'
	show_list(convert2(node6))

if __name__ == '__main__':
	test()
