#--coding=utf-8--

# 将复制含有随机指针节点的链表
# 【题目】
#     一种特殊的链表节点类描述如下：
#     public class Node {
#         public int value;
#         public Node next;
#         public Node rand;
#
#         public Node(int data) {
#             this.value = data;
#         }
#     }
#     Node 类中的 value 是节点值，next 指针和正常单链表中 next 指针的意义一样，都指向下一个节点，
# rand 指针是 Node 类中新增的指针，这个指针可能指向链表中的任意一个节点，也可能指向 null。
#     给定一个由 Node 节点类型组成的无环单链表的头节点 head，请实现一个函数完成这个链表中所有结构的复制，
# 并返回复制的新链表的头节点。例如：链表 1->2->3->null，假设 1 的 rand 指针指向 3，2 的 rand 指针指
# 向 null，3 的 rand 指针指向 1。复制后的链表应该也是这种结构，比如，1'->2'->3'->null，1' 的 rand 
# 指针指向 3'，2' 的 rand 指针指向 null，3' 的 rand 指针指向 1'，最后返回 1'。
#     进阶：不使用额外的数据结构，只用有限几个变量，且在时间复杂度为 O(N) 内完成原问题要实现的函数。

class Node(object):
	next = None
	rand = None
	def __init__(self, data):
		self.value = data

def copy_list_with_rand(head):
	dic = dict()
	cur = head
	while cur:
		dic[cur] = Node(cur.value)
		cur = cur.next
	cur = head
	while cur:
		dic.get(cur).next = dic.get(cur.next)
		dic.get(cur).rand = dic.get(cur.rand)
		cur = cur.next
	return dic.get(head)

def copy_list_with_rand2(head):
	if not head:
		return None
	cur = head
	next = None
	while cur:
		next = cur.next
		cur.next = Node(cur.value)
		cur.next.next = next
		cur = next
	cur = head
	cur_copy = None
	while cur:
		next = cur.next.next
		cur_copy = cur.next
		cur_copy.rand = cur.rand.next if cur.rand else None
		cur = next
	res = head.next
	cur = head
	while cur:
		next = cur.next.next
		cur_copy = cur.next
		cur.next = next
		cur_copy.next = next.next if next else None
		cur = next
	return res

def show_list(head):
	cur = head
	while cur:
		print cur.value, ' next:', cur.next.value if cur.next else 'None',\
		    ', rand:', cur.rand.value if cur.rand else 'None'
		cur = cur.next

def test():
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node1.next = node2
	node2.next = node3
	node1.rand = node3
	node3.rand = node1

	head = node1
	
	show_list(copy_list_with_rand(head))
	print '--------------------'
	show_list(copy_list_with_rand2(head))
	print '--------------------'
	show_list(head)

if __name__ == '__main__':
	test()
