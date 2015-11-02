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

class PetEnter(object):
	def __init__(self, pet, count):
		if isinstance(pet, Pet):
			self.pet = pet
			self.count = count
		else:
			raise 'err. not a pet'

	def get_pet(self):
		return self.pet

	def get_count(self):
		return self.count

	def get_pet_type(self):
		return self.pet.get_pet_type()

class CatDogQueue(object):
	dogQ = []
	catQ = []
	count = 0

	def add(self, pet):
		self.count = self.count + 1
		if isinstance(pet, Cat):
			self.catQ.append(PetEnter(pet, self.count))
		elif isinstance(pet, Dog):
			self.dogQ.append(PetEnter(pet, self.count))
		else:
			self.count = self.count - 1
			raise 'err. not a cat or a dog'

	def pollAll(self):
		if self.isEmpty():
			return None
		elif self.isCatEmpty():
			return self.pollDog()
		elif self.isDogEmpty():
			return self.pollCat()
		else:
			dog = self.dogQ[0]
			cat = self.catQ[0]
			if dog.count > cat.count:
				return self.pollCat()
			else:
				return self.pollDog()

	def pollDog(self):
		if self.isDogEmpty():
			return None
		first = self.dogQ[0]
		self.dogQ = self.dogQ[1:]
		return first.get_pet()

	def pollCat(self):
		if self.isCatEmpty():
			return None
		first = self.catQ[0]
		self.catQ = self.catQ[1:]
		return first.get_pet()

	def isEmpty(self):
		return (len(self.catQ) == 0) and (len(self.dogQ) == 0)

	def isDogEmpty(self):
		return len(self.dogQ) == 0

	def isCatEmpty(self):
		return len(self.catQ) == 0

def test():
	cat_dog_queue = CatDogQueue()
	dog1 = Dog()
	dog2 = Dog()
	cat1 = Cat()
	cat2 = Cat()
	cat_dog_queue.add(dog1)
	cat_dog_queue.add(cat1)
	cat_dog_queue.add(cat2)
	cat_dog_queue.add(dog2)
	print cat_dog_queue.pollAll()
	print cat_dog_queue.pollAll()
	print cat_dog_queue.pollCat()
	print cat_dog_queue.pollCat()
	print cat_dog_queue.pollDog()
	print cat_dog_queue.pollAll()

if __name__ == '__main__':
    test()
