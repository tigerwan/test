class mytest:
	@classmethod
	def get_class_name(cls):
		return cls.__name__

	def __init__(self):
		print("class name:{}".format(self.get_class_name()))

x=mytest()
