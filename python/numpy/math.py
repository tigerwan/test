import numpy

a = numpy.array([1, 2, 3, 4], float)
b = numpy.array([5, 6, 7, 8], float)

print(a + b)  # [  6.   8.  10.  12.]
print(numpy.add(a, b))  # [  6.   8.  10.  12.]

print(a - b)  # [-4. -4. -4. -4.]
print(numpy.subtract(a, b))  # [-4. -4. -4. -4.]

print(a * b)  # [  5.  12.  21.  32.]
print(numpy.multiply(a, b))  # [  5.  12.  21.  32.]

print(a / b)  # [ 0.2         0.33333333  0.42857143  0.5       ]
print(numpy.divide(a, b))  # [ 0.2         0.33333333  0.42857143  0.5       ]

print(a % b)  # [ 1.  2.  3.  4.]
print(numpy.mod(a, b))  # [ 1.  2.  3.  4.]

print(a**b)  # [  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(
    numpy.power(a, b)
)  # [  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]


my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.sum(my_array, axis = 0))         #Output : [4 6]
print(numpy.sum(my_array, axis = 1))         #Output : [3 7]
print(numpy.sum(my_array, axis = None))      #Output : 10
print(numpy.sum(my_array))                #Output : 10

print(numpy.prod(my_array, axis = 0))            #Output : [3 8]
print(numpy.prod(my_array, axis = 1))            #Output : [ 2 12]
print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(my_array))                      #Output : 24