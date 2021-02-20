l1=[]
x=0
numbers=int(input("enter the elements :"))
for i in range(numbers):
	l1.append(int(input("enter the values :")))
print(l1) 
for x in l1:  
    if x % 2 != 0: 
    	print(x, end = " ")
print()
		 
