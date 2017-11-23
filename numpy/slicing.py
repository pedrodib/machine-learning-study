# Slicing Array
l = [20, 30, 10, 40]
print(l[1:3])
print(l[1::2])
print(l[::2])

import numpy 

a = numpy.array(l)
print(a[1:3])
print(a[::2])

l2 = l[:]
print(l2)
l2[0] = 1000
print(l)
print(l2)

a2 = a[:]
print(a)
a2[0] = 1000
print(a)
print(a2)

#copias de array:
c = a.copy()
print(c)
c[0] = 1000000
print(c)
print(a)
