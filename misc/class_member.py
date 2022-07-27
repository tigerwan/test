class c1():
	c_v1=0
	def __init__(self):
		self.o_v1=100

	def update_in_obj(self):
		self.c_v1=100

	@classmethod
	def update_in_classmethod(cls):
		cls.c_v1=200

	def update_class(self):
		c1.c_v1=300

	def update_class2(self):
		self.__class__.c_v1=400

obj = c1()
print('update class member in class method')
obj.update_in_classmethod()
print(obj.__dict__)
print(c1.__dict__)

print('update class member with class name')
obj.update_class()
print(obj.__dict__)
print(c1.__dict__)

print('update class member with __class__')
obj.update_class2()
print(obj.__dict__)
print(c1.__dict__)

print('update class member in object method')
obj.update_in_obj()
print(obj.__dict__)
print(c1.__dict__)
