#--coding=utf-8--

# 删除无序单链表中值重复出现的节点
# 【题目】
#     给定一个无序单链表的头节点 head，删除其中值重复出现的节点。
#     例如：1->2->3->3->4->4->2->1->1->null，删除值重复的节点之后为 1->2->3->4->null。
#     请按以下要求实现两种方法。
#     方法1：如果链表长度为 N，时间复杂度达到 O(N)。
#     方法2：额外空间复杂度为 O(1)。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def remove_rep(head):
	if not head:
		return
	record = []
	record.append(head.value)
	pre, cur = head, head
	while cur.next:
		cur = cur.next
		if cur.value in record:
			pre.next = cur.next
			cur = pre
		else:
			record.append(cur.value)
			pre = cur

def remove_rep2(head):
	if not head:
		return
	cur = head
	pre, next = None, None
	while cur:
		pre = cur
		next = cur.next
		while next:
			if cur.value == next.value:
				pre.next = next.next
			else:
				pre = next
			next = next.next
		cur = cur.next

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
	print 'remove_rep:',
	remove_rep2(head)
	show_list(head)

if __name__ == '__main__':
	test()
