#--coding=utf-8--

class Mystack(object):
	data_stack = []
	min_stack = []

	def push(self, num):
		self.data_stack.append(num)
		if not self.min_stack:
			self.min_stack.append(num)
		elif num <= self.get_min():
			self.min_stack.append(num)

	def pop(self):
		num = self.data_stack.pop()
		if num == self.get_min():
			self.min_stack.pop()
		return num

	def get_min(self):
		return self.min_stack[-1]

def test():
	stack = Mystack()
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