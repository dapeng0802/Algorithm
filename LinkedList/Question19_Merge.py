#--coding=utf-8--

# 合并两个有序的单链表
# 【题目】
#     给定两个有序单链表的头节点 head1 和 head2，请合并两个有序链表，合并后的链表依然有序，
# 并返回合并后链表的头节点。
#     例如：
#     0->2->3->7->null
#     1->3->5->7->9->null
#     合并后的链表为：0->1->2->3->3->5->7->7->9->null

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def merge(head1, head2):
	if not head1 or not head2:
		return head1 if head1 else head2
	head = head1 if head1.value < head2.value else head2
	pre, next = None, None
	cur1 = head1 if head1 == head else head2
	cur2 = head2 if head1 == head else head1
	while cur1 and cur2:
		if cur1.value <= cur2.value:
			pre = cur1
			cur1 = cur1.next
		else:
			next = cur2.next
			pre.next = cur2
			cur2.next = cur1
			pre = cur2
			cur2 = next
	pre.next = cur1 if cur1 else cur2
	return head
	
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
	nodes = [Node(1), Node(3), Node(4), Node(6), Node(7), Node(9), Node(12), Node(12), Node(14)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	head1 = nodes[0]

	nodes = [Node(2), Node(3), Node(5), Node(8), Node(10), Node(11), Node(13), Node(14), Node(15)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	head2 = nodes[0]
	
	print 'head1:'
	show_list(head1)
	print 'head2:'
	show_list(head2)
	print 'merged:'
	show_list(merge(head1, head2))

if __name__ == '__main__':
	test()
