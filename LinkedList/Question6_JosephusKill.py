#--coding=utf-8--

# 环形单链表的约瑟夫问题
# 【题目】
#     据说著名犹太历史学家 Josephus 有过以下故事：在罗马人占领桥塔帕特后，39 个犹太人与 Josephus 及他的朋友
# 躲到一个洞中，39 个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41 个人排成一个圆圈，由第 1 个人
# 开始报数，报数到 3 的人就自杀，然后再由下一个人重新报 1，报数到 3 的人再自杀，这样依次下去，直到剩下最后一个人
# 时，那个人可以自由选择自己的命运。这就是著名的约瑟夫问题。现在请用单向链表描述该结构并呈现整个自杀过程。
#     输入：一个环形单向链表的头节点 head 和报数的值 m。
#     返回：最后生存下来的节点，且这个节点自己组成的环形单向链表，其他节点都删掉。
#     进阶：如果链表节点数为 N，想在时间复杂度为 O(N) 时完成原问题的要求，该怎么实现？

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def josephus_kill(head, m):
	if not head or m < 1:
		return head
	count = 0
	cur = head
	while cur.next != cur:
		count += 1
		if count == m - 1:
			count = 0
			cur.next = cur.next.next
		cur = cur.next
	return cur

def josephus_kill2(head, m):
	if not head or head.next == head or m < 1:
		return head
	last = head
	while last.next != head:
		last = last.next
	count = 0
	while head != last:
		count += 1
		if count == m:
			last.next = head.next
			count = 0
		else:
			last = last.next
		head = last.next
	return head

def josephus_kill3(head, m):
	if not head or head.next == head or m < 1:
		return head
	cur = head.next
	size = 1
	while cur != head:
		size += 1
		cur = cur.next
	live = get_live(size, m)
	while live != 1:
		live -= 1
		head = head.next
	head.next = head
	return head

def get_live(i, m):
	if i == 1:
		return 1
	return (get_live(i - 1, m) + m - 1) % i + 1

def show_list(head):
	cur = head.next
	print head.value,
	while cur != head:
		print '->', cur.value,
		cur = cur.next
	print ''

def test():
	head = Node(0)
	cur = head
	for i in range(1, 41):
		cur.next = Node(i)
		cur = cur.next
	cur.next = head
	show_list(head)
	head = josephus_kill3(head, 3)
	show_list(head)
	

if __name__ == '__main__':
	test()