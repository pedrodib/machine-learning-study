import numpy

a = numpy.array([10,20,30,40])
print(a)

mat = numpy.array([[1,2], [3,4]])
print(mat[1][1])
print(mat.transpose())

m1 = numpy.array([[1, 2], [3, 4]])
m2 = numpy.array([[5, 6], [7, 8]])
print(m1 + m2)
print(m1 - m2)
print(m1 * m2)

m3 = numpy.array([1, 2, 3, 4])
print(m3.sum())
print(m3.argmax())
print(m3.argmin())