class c1():
	x=1
	def __init__(self):
		self.y=2

class c2(c1):
	def __init__(self):
		super().__init__()
	
class c3(c1):
	def __init__(self):
		super().__init__()


o1=c1()
o2=c2()
o3=c3()


print('c1.x={} vs c2.x={} vs c3.x={}'.format(c1.x, c2.x, c3.x))
c2.x=100
print('c1.x={} vs c2.x={} vs c3.x={}'.format(c1.x, c2.x, c3.x))
print('c1.__dict__={} vs c2.__dict__={} vs c3.__dict__={}'.format(c1.__dict__, c2.__dict__, c3.__dict__))


print('o1.x={} vs o2.x={} vs o3.x={}'.format(o1.x, o2.x, o3.x))
o2.x=400
print('o1.x={} vs o2.x={} vs o3.x={}'.format(o1.x, o2.x, o3.x))
o1.y=1000
print('o1.y={} vs o2.y={} vs o3.y={}'.format(o1.y, o2.y, o3.y))
