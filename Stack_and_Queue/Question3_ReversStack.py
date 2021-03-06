#--coding=utf-8--

# 如何仅用递归函数和栈操作逆序一个栈
# 【题目】
#     一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1，
# 将这个栈转置后，从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，
# 但是只能用递归函数来实现，不能用其他数据结构。

class Stack(object):
    def __init__(self):
        self.stack_object = []

    def push(self, num):
        self.stack_object.append(num)

    def pop(self):
        return self.stack_object.pop()

    def is_empty(self):
        return (len(self.stack_object) == 0)

def remove_last_element(stack):
    result = stack.pop()
    if stack.is_empty():
        return result
    last = remove_last_element(stack)
    stack.push(result)
    return last

def reverse(stack):
    if stack.is_empty():
        return
    last = remove_last_element(stack)
    reverse(stack)
    stack.push(last)

def test():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    reverse(stack)
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()

if __name__ == '__main__':
    test()
