x=int(input("Enter the element :"))
d1={}
def Merge(d1, d2):
    return(d2.update(d1))
for i in range(x):
	keys=input("Enter the keys :")
	values=input("Enter the values :")
	d1[keys]=values
print(d1)
y=int(input("Enter the element :"))
d2={}	
for i in range(y):
	keys=input("Enter the keys :")
	values=input("Enter the values :")
	d2[keys]=values
print(d2)	
print(d1.update(d2))
print(d1)	