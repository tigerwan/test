class p:
	def __init__(self):
		self.x=100

class c(p): 
	def __init__(self):
		self.x=200

obj_c=c()
print(obj_c.x)
