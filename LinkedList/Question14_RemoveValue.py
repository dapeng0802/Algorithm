#--coding=utf-8--

# 在单链表中删除指定值的节点
# 【题目】
#     给定一个链表的头节点 head 和一个整数 num，请实现函数将值为 num 的节点全部删除。
#     例如：链表为 1->2->3->4->null，num=3，链表调整后为：1->2->4->null。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def remove_value(head, num):
	if not head:
		return head
	stack = []
	while head:
		if head.value != num:
			stack.append(head)
		head = head.next
	while len(stack):
		stack[-1].next = head
		head = stack.pop()
	return head

def remove_value2(head, num):
	if not head:
		return head
	new_head = None
	pre, cur = head, head
	while cur:
		if num == cur.value:
			pre.next = cur.next
		else:
			if not new_head:
				new_head = cur
			pre = cur
		cur = cur.next
	return new_head

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
	nodes = [Node(1), Node(2), Node(3), Node(3), Node(4), Node(4), Node(2), Node(1), Node(1)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head = nodes[0]
	
	print 'head:',
	show_list(head)
	print 'remove_value:',
	show_list(remove_value2(head, 1))

if __name__ == '__main__':
	test()
