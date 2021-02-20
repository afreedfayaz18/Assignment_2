x=int(input("Enter the element :"))
d1={}
for i in range(x):
	keys=input("Enter the keys :")
	values=input("Enter the values :")
	d1[keys]=values
for values in d1:
    x.append(values)
print(d1)