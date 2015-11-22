#--coding=utf-8--

# 将单向链表按某值划分成左边小、中间相等、右边大的形式
# 【题目】
#     给定一个单向链表的头节点 head，节点的值类型是整型，再给定一个整数 pivot，实现一个调整链表的函数，
# 将链表调整为左部分都是值小于 pivot 的节点，中间部分都是值等于 pivot 的节点，右部分都是值大于 pivot 的节点。
# 除这个要求外，对调整后的节点顺序没有更多的要求。
#     例如：链表 9->0->4->5->1，pivot=3。
#     调整后链表可以是 1->0->4->9->5，也可以是 0->1->9->5->4。总之，满足左部分都是小于 3 的节点，
# 中间部分都是等于 3 的节点（本例中这个部分为空），右部分都是大于 3 的节点即可。对某部分内部的节点顺序不做要求。
#     进阶：
#     在原问题的要求之上再增加如下两个要求。
#     1. 在左、中、右三个部分的内部也做顺序要求，要求每部分里的节点从左到右的顺序与原链表中节点的先后次序一致。
#     例如：链表 9->0->4->5->1，pivot=3。调整后的链表是 0->1->9->4->5。在满足原问题要求的同时，
# 左部分节点从左到右为0、1。在原链表中也是先出现0，后出现1；中间部分在本例中为空，不再讨论；
# 右部分节点从左到右为9、4、5。在原链表中也是先出现9，然后出现4，最后出现5。
#     2. 如果链表长度为 N，时间复杂度请达到 O(N)，额外空间复杂度请达到 O(1)。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def list_partition(head, pivot):
	if not head:
		return head
	node_arr = []
	cur = head
	while cur:
		node_arr.append(cur)
		cur = cur.next
	arr_partition(node_arr, pivot)
	for i in range(1,len(node_arr)):
		node_arr[i - 1].next = node_arr[i]
	node_arr[i].next = None
	return node_arr[0]

def arr_partition(node_arr, pivot):
	small = -1
	big = len(node_arr)
	index = 0
	while index != big:
		if node_arr[index].value < pivot:
			small += 1
			swap(node_arr, small, index)
			index += 1
		elif node_arr[index].value == pivot:
			index += 1
		else:
			big -= 1
			swap(node_arr, big, index)

def swap(node_arr, a, b):
	tmp = node_arr[a]
	node_arr[a] = node_arr[b]
	node_arr[b] = tmp

def list_partition2(head, pivot):
	sH, sH, eH, eT, bH, bT, next = None, None, None, None, None, None, None
	while head:
		next = head.next
		head.next = None
		if head.value < pivot:
			if not sH:
				sH = head
				sT = head
			else:
				sT.next = head
				sT = head
		elif head.value == pivot:
			if not eH:
				eH = head
				eT = head
			else:
				eT.next = head
				eT = head
		else:
			if not bH:
				bH = head
				bT = head
			else:
				bT.next = head
				bT = head
		head = next
	if sT:
		sT.next = eH
		eT = eT if eT else sT
	if eT:
		eT.next = bH
	return sH if sH else eH if eH else bH

def show_list(head):
	cur = head.next
	print head.value,
	while cur:
		print '->', cur.value,
		cur = cur.next
	print ''

def test():
	nodes = [Node(9), Node(0), Node(4), Node(5), Node(1)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head = nodes[0]
	
	show_list(head)
	head = list_partition(head, 3)
	show_list(head)

	nodes = [Node(7), Node(9), Node(1), Node(8), Node(5), Node(2), Node(5)]
	for i in range(1, len(nodes)):
		nodes[i - 1].next = nodes[i]
	nodes[i].next = None
	head = nodes[0]
	
	show_list(head)
	head = list_partition2(head, 5)
	show_list(head)

if __name__ == '__main__':
	test()
