#--coding=utf-8--

# 设计一个有 getMin 功能的栈
# 【题目】
# 	实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
# 【要求】
# 	1. pop、push、getMin 操作的时间复杂度都是 O(1)
# 	2. 设计的栈类型可以使用现成的栈结构

class MyStack(object):
	data_stack = []
	min_stack = []

	def push(self, num):
		self.data_stack.append(num)
		if not self.min_stack:
			self.min_stack.append(num)
		elif num <= self.get_min():
			self.min_stack.append(num)

	def pop(self):
		if not self.data_stack:
			return None
		num = self.data_stack.pop()
		if num == self.get_min():
			self.min_stack.pop()
		return num

	def get_min(self):
		if not self.data_stack:
			return None
		return self.min_stack[-1]

# 解法2：
class MyStack2(object):
	data_stack = []
	min_stack = []

	def push(self, num):
		self.data_stack.append(num)
		if not self.min_stack:
			self.min_stack.append(num)
		elif num < self.get_min():
			self.min_stack.append(num)
		else:
			self.min_stack.append(self.min_stack[-1])
	def pop(self):
		if not self.data_stack:
			return None
		self.min_stack.pop()
		return self.data_stack.pop()

	def get_min(self):
		if not self.data_stack:
			return None
		return self.min_stack[-1]

def test():
	stack = MyStack()
	stack.push(3)
	stack.push(4)
	stack.push(5)
	stack.push(1)
	stack.push(2)
	stack.push(1)
	print 'min:', stack.get_min()
	print stack.pop()
	print stack.pop()
	print stack.pop()
	print 'min:', stack.get_min()

if __name__ == '__main__':
	test()