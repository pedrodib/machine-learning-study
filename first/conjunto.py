s = set()
s.add(10)
s.add(20)
s.add(30)
s.add(10)
print(s)

s1 = {1,2,3,4}
s2 = {3,4,5,6}
union = s1.union(s2)
print(union)

inter = s1.intersection(s2)
print(inter)

diff = s1.difference(s2)
print(diff)

#Example
list = [1,2,3,3,3,4,4,4,5,5,6,6,7,8,9,9]
s = set(list)
print(s)