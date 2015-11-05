#--coding=utf-8--

# 用一个栈实现另一个栈的排序
# 【题目】
#     一个栈中元素的类型为整型，现在想将该栈从顶到底按从大到小的顺序排序，只许申请一个栈。
# 除此之外，可以申请新的变量，但不能申请额外的数据结构。如何完成排序？

def sort_stack_by_stack(stack):
	help_stack = []
	while len(stack) > 0:
		item = stack.pop()
		while len(help_stack) > 0 and item > help_stack[-1]:
			stack.append(help_stack.pop())
		help_stack.append(item)
	while len(help_stack) > 0:
		stack.append(help_stack.pop())

def test():
	stack = [1, 4, 5, 6, 2, 8, 9, 3]
	sort_stack_by_stack(stack)
	print stack

if __name__ == '__main__':
	test()
