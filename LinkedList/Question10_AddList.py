#--coding=utf-8--

# 两个单链表生成相加链表
# 【题目】
#     假设链表中每一个节点的值都在 0~9 之间，那么链表整体就可以代表一个整数。
#     例如：9->3->7，可以代表整数 937。
#     给定两个这种链表的头节点 head1 和 head2，请生成代表两个整数相加值的结果链表。
#     例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def add_list(head1, head2):
	stack1 = []
	stack2 = []
	cur = head1
	while cur:
		stack1.append(cur.value)
		cur = cur.next
	cur = head2
	while cur:
		stack2.append(cur.value)
		cur = cur.next
	tmp = 0
	node, pre = None, Node
	while len(stack1) or len(stack2):
		tmp = (stack1.pop() if len(stack1) else 0) + (stack2.pop() if len(stack2) else 0) + tmp
		pre = node
		node = Node(tmp % 10)
		node.next = pre
		tmp = tmp / 10
	if tmp:
		pre = node
		node = Node(tmp)
		node.next = pre
	
	return node

def add_list2(head1, head2):
	head1 = reverse_list(head1)
	head2 = reverse_list(head2)
	tmp = 0
	cur1, cur2 = head1, head2
	pre, node = None, None
	while cur1 or cur2:
		tmp = (cur1.value if cur1 else 0) + (cur2.value if cur2 else 0) + tmp
		pre = node
		node = Node(tmp % 10)
		node.next = pre
		cur1 = cur1.next if cur1 else None
		cur2 = cur2.next if cur2 else None
		tmp = tmp / 10
	if tmp:
		pre = node
		node = Node(tmp)
		node.next = pre
	reverse_list(head1)
	reverse_list(head2)
	return node

def reverse_list(head):
	pre, next = None, None
	while head:
		next = head.next
		head.next = pre
		pre = head
		head = next
	return pre

def show_list(head):
	if not head:
		return
	cur = head.next
	print head.value,
	while cur:
		print '->', cur.value,
		cur = cur.next
	print ''

def test():
	nodes = [Node(1), Node(3), Node(5)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head1 = nodes[0]
	nodes = [Node(2), Node(4), Node(6)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head2 = nodes[0]
	
	print 'head1:',
	show_list(head1)
	print 'head2:',
	show_list(head2)
	print '(by add_list)head1 + head2:',
	show_list(add_list(head1, head2))
	print '(by add_list2)head1 + head2:',
	show_list(add_list2(head1, head2))
	print 'head1:',
	show_list(head1)
	print 'head2:',
	show_list(head2)
	

if __name__ == '__main__':
	test()
