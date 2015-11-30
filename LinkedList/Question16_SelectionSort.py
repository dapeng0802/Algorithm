#--coding=utf-8--

# 单链表的选择排序
# 【题目】
#     给定一个无序单链表的头节点 head，实现单链表的选择排序。
# 【要求】
#     额外空间复杂度为 O(1)。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def selection_sort(head):
	tail = None
	cur = head
	small_pre, small = None, None
	while cur:
		small = cur
		small_pre = get_smallest_pre_node(cur)
		if small_pre:
			small = small_pre.next
			small_pre.next = small.next
		cur = cur.next if cur == small else cur
		if not tail:
			head = small
		else :
			tail.next = small
		tail = small
	return head

def get_smallest_pre_node(head):
	small_pre = None
	small, pre = head, head
	cur = head.next
	while cur:
		if cur.value < small.value:
			small_pre = pre
			small = cur
		pre = cur
		cur = cur.next
	return small_pre
	
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
	print 'sorted:'
	show_list(selection_sort(head))

if __name__ == '__main__':
	test()
