#--coding=utf-8--

# 由两个栈组成的队列
# 【题目】
# 	编写一个类，用两个栈实现队列，支持队列的基本操作（add、poll、peek）。

class MyQueue(object):
	push_stack = []
	pop_stack = []

	def add(self, num):
		if not self.pop_stack:
			self.push_stack.append(num)
			while self.push_stack:
				self.pop_stack.append(self.push_stack.pop())
		else:
			while self.pop_stack:
				self.push_stack.append(self.pop_stack.pop())
			self.add(num)

	def poll(self):
		if not self.pop_stack:
			return None
		return self.pop_stack.pop()

	def peek(self):
		if not self.pop_stack:
			return None
		return self.pop_stack[-1]

# 以上是我想到的解法，看了书中的解法才意识到我在 add 元素的时候折腾得太繁琐了，
# 两个栈没有充分运用起来，始终保持着其中一个栈为空的状态。--!
# 其实在 poll 和 peek 的再时候进行弹出栈的判断更好，MyQueue2是书中解法的Python实现：

class MyQueue2(object):
	push_stack = []
	pop_stack = []

	def add(self, num):
		self.push_stack.append(num)

	def poll(self):
		if not (self.push_stack or self.pop_stack):
			return None
		if not self.pop_stack:
			while self.push_stack:
				self.pop_stack.append(self.push_stack.pop())
		return self.pop_stack.pop()

	def peek(self):
		if not (self.push_stack or self.pop_stack):
			return None
		if not self.pop_stack:
			while self.push_stack:
				self.pop_stack.append(self.push_stack.pop())
		return self.pop_stack[-1]

def test():
	queue = MyQueue2()
	queue.add(1)
	queue.add(2)
	queue.add(3)
	queue.add(4)
	queue.add(5)
	print 'poll', queue.poll()
	print 'peek', queue.peek()
	print 'poll', queue.poll()
	print 'peek', queue.peek()
	print 'poll', queue.poll()
	print 'peek', queue.peek()
	print 'poll', queue.poll()
	print 'peek', queue.peek()
	print 'poll', queue.poll()
	print 'peek', queue.peek()
	print 'poll', queue.poll()

if __name__ == '__main__':
	test()