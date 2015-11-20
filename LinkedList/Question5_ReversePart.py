#--coding=utf-8--

# 反转部分单向链表
# 【题目】
#     给定一个单向链表的头节点 head，以及两个整数 from 和 to，在单向链表上把第 from 个节点到第 to 个节点的一部分进行反转。
#     例如：
#     1->2->3->4->5->null，from=2，to=4
#     调整结果为：1->4->3->2->5->null
#     再如：
#     1->2->3->null，from=1，to=3
#     调整结果为：3->2->1->null
# 【要求】
#     1. 如果链表长度为 N，时间复杂度要求为 O(N)，额外空间复杂度要求为 O(1)。
#     2. 如果不满足 1<=from<=to<=N，则不用调整。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def reverse_part(head, from_pos, to_pos):
	length = 0
	temp = head
	fPre, tPos = None, None
	while temp:
		length += 1
		fPre = temp if length == from_pos - 1 else fPre
		tPos = temp if length == to_pos + 1 else tPos
		temp = temp.next
	if from_pos > to_pos or from_pos < 1 or to_pos > length:
		return head
	temp = fPre.next if fPre else head
	new_head = temp.next
	temp.next = tPos
	next = None
	while new_head != tPos:
		next = new_head.next
		new_head.next = temp
		temp = new_head
		new_head = next
	if fPre:
		fPre.next = temp
		return head
	return temp


def show_list(head):
	cur = head
	while cur:
		print cur.value, '->',
		cur = cur.next
	print 'None'

def test():
	head = Node(0)
	cur = head
	for i in range(1, 10):
		cur.next = Node(i)
		cur = cur.next
	show_list(head)
	head = reverse_part(head, 3, 8)
	show_list(head)
	head = reverse_part(head, 1, 8)
	show_list(head)
	head = reverse_part(head, 3, 10)
	show_list(head)
	head = reverse_part(head, 1, 10)
	show_list(head)
	head = reverse_part(head, 1, 12)
	show_list(head)

if __name__ == '__main__':
	test()