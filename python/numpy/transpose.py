import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(numpy.transpose(my_array))
print(my_array.swapaxes(1,0))