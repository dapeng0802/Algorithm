#--coding=utf-8--

# 一种怪异的节点删除方式
# 【题目】
#     链表节点值类型为 int 型，给定一个链表中的节点 node，但不给定整个链表的头节点。
# 如何在链表中删除 node？请实现这个函数，并分析这么会出现哪些问题。
# 【要求】
#     时间复杂度为 O(1)。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def remove_node_wired(node):
	if not node:
		return
	if node.next:
		node.value = node.next.value
		node.next = node.next.next
	else:
		node = None # 如果 node 为最后一个节点，该节点是无法删除的，将该节点置为 None 是无用的。
	
def show_list(head):
	if not head:
		return
	cur = head.next
	print head.value,
	while cur:
		print '->', cur.value,
		cur = cur.next
	print '-> None'

def test():
	nodes = [Node(7), Node(4), Node(3), Node(6), Node(2), Node(1), Node(8), Node(3), Node(5)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head = nodes[0]
	
	print 'head:'
	show_list(head)
	print ''
	print 'remove_node_wired:'
	remove_node_wired(nodes[6])
	show_list(head)

if __name__ == '__main__':
	test()
