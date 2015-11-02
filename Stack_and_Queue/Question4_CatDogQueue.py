#--coding=utf-8--

# 猫狗队列
# 【题目】
#     宠物、猫、狗的类如下：
#     public class Pet {
#         private String type;
#
# 	      public Pet(String type) {
# 	          this.type = type;
# 	      }

# 	      public String getPetType() {
# 	          return this.type
# 	      }
#     }
#
#     public class Dog extends Pet {
# 	      public Dog() {
# 	          super("dog");
# 	      }
#     }
#
#     public class Cat extends Pet {
# 	      public Cat() {
# 	          super("cat");
# 	      }
#     }
#
#     实现一种猫狗队列的结构，要求如下：
#     1. 用户可以调用 add 方法将 cat 类或者 dog 类的实例放入队列中；
#     2. 用户可以调用 pollAll 方法，将队列中所有的实例按照进队列的先后顺序依次弹出；
#     3. 用户可以调用 pollDog 方法，将队列中 dog 类的实例按照进队列的先后顺序依次弹出；
#     4. 用户可以调用 pollCat 方法，将队列中 cat 类的实例按照进队列的先后顺序依次弹出；
#     5. 用户可以调用 isEmpty 方法，检查队列中是否还有都 dog 或 cat 的实例；
#     6. 用户可以调用 isDogEmpty 方法，检查队列中是否有 dog 类的实例；
#     7. 用户可以调用 isCatEmpty 方法，检查队列中是否有 cat 类的实例。

# 以上问题描述为书中Java语言的题目，因此需要用Python语言再实现 Pet、Dog、Cat 类
class Pet(object):
	type = ''

	def __init__(self, type):
		self.type = type

	def get_pet_type(self):
		return self.type

class Dog(Pet):
	def __init__(self):
		super(Dog, self).__init__('dog')

class Cat(Pet):
	def __init__(self):
		super(Cat, self).__init__('cat')

def test():
	dog = Dog()
	cat = Cat()
	print dog.get_pet_type()
	print cat.get_pet_type()

if __name__ == '__main__':
    test()
