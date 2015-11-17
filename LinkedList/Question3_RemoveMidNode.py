#--coding=utf-8--

# 删除链表的中间节点和 a/b 处的节点
# 【题目】
#     给定链表的头节点 head，实现删除链表的中间节点的函数。
#     例如：
#     不删除任何节点；
#     1->2，删除节点1；
#     1->2->3，删除节点2；
#     1->2->3->4，删除节点2；
#     1->2->3->4->5，删除节点3；
#     进阶：
#     给定链表的头节点 head、整数 a 和 b，实现删除位于 a/b 处节点的函数。
#     例如：
#     链表：1->2->3->4->5，假设 a/b 的值为 r。
#     如果 r 等于0，不删除任何节点；
#     如果 r 在区间(0, 1/5]上，删除节点1；
#     如果 r 在区间(1/5, 2/5]上，删除节点2；
#     如果 r 在区间(2/5, 3/5]上，删除节点3；
#     如果 r 在区间(3/5, 4/5]上，删除节点4；
#     如果 r 在区间(4/5, 1]上，删除节点5；
#     如果 r 大于1，不删除任何节点。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def remove_mid_node(head):
	if head and head.next:
		if head.next.next:
			pre = head
			cur = head.next.next
			while cur.next and cur.next.next:
				pre = pre.next
				cur = cur.next.next
			pre.next = pre.next.next
		else:
			return head.next
	
	return head

def remove_adivb_node(head, a, b):
	if head and a > 1 and a < b:
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next
		n = int((a * n + b - 1) / b) #UP(a/b) = int((a+b-1)/b) 向上取整
		if n == 1:
			head = head.next
		if n > 1:
			cur = head
			while n - 1 != 1:
				cur = cur.next
				n -= 1
			cur.next = cur.next.next

	return head

def test():
	head = Node(0)
	cur = head
	for i in range(1, 20):
		cur.next = Node(i)
		cur = cur.next
	head = remove_mid_node(head)
	cur = head
	while cur:
		print cur.value, '->',
		cur = cur.next
	print ''
	head = remove_adivb_node(head, 3, 9)
	cur = head
	while cur:
		print cur.value, '->',
		cur = cur.next
	print ''


if __name__ == '__main__':
	test()