x=int(input("Enter the element :"))
dict={} 
for i in range(x):
	keys=int(input("Enter the keys :"))
	values=(keys*keys)
	dict[keys]=values
print(dict)	