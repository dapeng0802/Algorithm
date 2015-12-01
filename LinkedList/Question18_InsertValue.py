#--coding=utf-8--

# 向有序的环形单链表中插入新节点
# 【题目】
#     一个环形单链表从头节点 head 开始不降序，同时由最后的节点指回头节点。给定这样一个环形单链表的头节点 head
# 和一个整数 num，请生成节点值为 num 的新节点，并插入到这个环形链表中，保证调整后的链表依然有序。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def insert_value(head, num):
	node = Node(num)
	if not head:
		node.next = node
		return node
	pre, cur = head, head.next
	while not (cur == head):
		if pre.value <= num and cur.value >= num:
			break
		pre = cur
		cur = cur.next
	pre.next = node
	node.next = cur
	return head if head.value < num else node
	
def show_list(head):
	if not head:
		return
	cur = head.next
	print head.value,
	while cur.value != head.value:
		print '->', cur.value,
		cur = cur.next
	print '-> None'

def test():
	nodes = [Node(1), Node(3), Node(4), Node(6), Node(7), Node(9), Node(12), Node(12), Node(14)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = nodes[0]
	head = nodes[0]
	
	print 'head:'
	show_list(head)
	print 'insert 0:'
	head = insert_value(head, 0)
	show_list(head)
	print 'insert 8:'
	head = insert_value(head, 8)
	show_list(head)
	print 'insert 15:'
	head = insert_value(head, 15)
	show_list(head)

if __name__ == '__main__':
	test()
