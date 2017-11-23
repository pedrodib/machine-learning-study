dev_name 	= "Pedro"
age 		= 21
approved	= True
price_byHour = 30.524564
print(dev_name)
print(id(dev_name))
print(type(dev_name))
print(len(dev_name))
print(dev_name.__len__())
print("%s it's %d years old" % (dev_name, age))
print("He cost US$ %.2f per hour" % price_byHour)