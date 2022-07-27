
import numpy
A = numpy.array([1,2.3,4,5],int)
B = numpy.array([10,11,12],int)
print(numpy.concatenate((A, B), axis = 0))