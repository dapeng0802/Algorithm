#--coding=utf-8--

# 按照左右半区的方式重新组合单链表
# 【题目】
#     给定一个单链表的头节点 head，链表长度为 N，如果 N 为偶数，那么前 N/2 个节点算作左半区，后 N/2 个节点算作右半区；
# 如果 N 为奇数，那么前 N/2 个节点算作左半区，后 N/2+1 个节点算作右半区。左半区从左到右依次记为 L1->L2->L3->...，
# 右半区从左到右记为 R1->R2->R3->...，请将单链表调整成 L1->R1->L2->R2->L3->R3... 的形式。
#     例如：
#     1->null，调整为 1->null。
#     1->2->null，调整为 1->2->null。
#     1->2->3->null，调整为 1->2->3->null。
#     1->2->3->4->null，调整为 1->3->2->4->null。
#     1->2->3->4->5->null，调整为 1->3->2->4->5->null。
#     1->2->3->4->5->6->null，调整为 1->4->2->5->3->6->null。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

	def __cmp__(self, cmpres):
		return cmp(cmp(id(self), id(cmpres)), 0)

def relocate(head):
	if not head:
		return
	cur = head
	count = 0
	while cur:
		count += 1
		cur = cur.next
	if count <= 3:
		return head
	cur = head
	count1 = 0
	while cur:
		count1 += 1
		if count1 == count / 2:
			half = cur.next
			break
		cur = cur.next
	cur1, cur2 = head, half
	next1, next2, pre = None, None, None
	while cur1 != half:
		next1 = cur1.next
		next2 = cur2.next
		cur2.next = next1
		cur1.next = cur2
		pre = cur2
		cur2 = next2
		cur1 = next1
	pre.next = cur2

def relocate2(head):
	if not head or not head.next:
		return
	mid = head
	right = head.next
	while right.next and right.next.next:
		mid = mid.next
		right = right.next.next
	right = mid.next
	mid.next = None
	next = None
	while head.next:
		next = right.next
		right.next = head.next
		head.next = right
		head = right.next
		right = next
	head.next = right

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
	nodes = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	head = nodes[0]
	
	print 'head:'
	show_list(head)
	print 'relocate:'
	relocate2(head)
	show_list(head)

if __name__ == '__main__':
	test()
