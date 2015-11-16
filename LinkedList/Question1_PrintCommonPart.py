#--coding=utf-8--

# 打印两个有序链表的公共部分
# 【题目】
#     给定两个有序链表的头指针 head1 和 head2，打印两个链表的公共部分。

class Node(object):
	next = None
	def __init__(self, data):
		self.value = data

def print_common_part(head1, head2):
	print 'Common Part: ',
	while head1 and head2:
		if head1.value < head2.value:
			head1 = head1.next
		elif head1.value > head2.value:
			head2 = head2.next
		else:
			print head1.value,
			head1 = head1.next
			head2 = head2.next

def test():
	head1 = Node(0)
	head2 = Node(0)
	temp1 = head1
	temp2 = head2
	for i in range(1, 50, 2):
		temp1.next = Node(i)
		temp1 = temp1.next
	for i in range(1, 50, 3):
		temp2.next = Node(i)
		temp2 = temp2.next

	print_common_part(head1, head2)

if __name__ == '__main__':
	test()