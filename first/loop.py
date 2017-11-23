# WHILE
i = 1
while i <= 10:
	if i%2 == 0:
		print(i)
	i += 1
	# break -> stop while

#FOR
for i in xrange(0,10, 3):
	print(i)

# FOREACH
list = [1, 10, 3, 4]
search = 10
for e in list:
	if e == search:
		print("Founded!")
		break
