def starts_with_A(s):
    return s[0] == "A"
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
print(fruit)
map_object = map(lambda s: s[0] == "A", fruit)
print(list(map_object))


filter_object = filter(starts_with_A, fruit)
print(fruit)
print(list(filter_object))


from functools import reduce

def add(x, y):
    return x + y

list1 = [2, 4, 7, 3]
print(list1)
print(reduce(add, list1))
    