print("Python List append()")
animals = ['cat', 'dog', 'rabbit']
print(animals)
animals.append('guinea pig')
print('Updated animals list: ', animals)

print("Python List copy()")
old_list = [1, 2, 3]
new_list = old_list
new_list.append('a')
print('New List:', new_list)
print('Old List:', old_list)

print("Python List count()")
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
print(vowels)
count = vowels.count('i')
print('The count of i is:', count)
count = vowels.count('p')
print('The count of p is:', count)

print("Python List extend()")
languages = ['French', 'English']
print(languages)
languages1 = ['Spanish', 'Portuguese']
print(languages1)
languages.extend(languages1)
print('Languages List:', languages)

print("Python List index()")
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
print(vowels)
index = vowels.index('e')
print('The index of e:', index)
index = vowels.index('i')
print('The index of i:', index)

print("Python List insert()")
vowel = ['a', 'e', 'i', 'u']
print(vowel)
vowel.insert(3, 'o')
print('Updated List:', vowel)

print("Python List pop()")
language = ['Python', 'Java', 'C++', 'French', 'C']
print(language)
return_value = language.pop(3)
print('Return Value:', return_value)
print('Updated List:', languages)

print("Python List remove()")
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
print(animals)
animals.remove('rabbit')
print('Updated animals list: ', animals)

print("Python List reverse()")
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
systems.reverse()
print('Updated List:', systems)

print("Python List sort()")
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print('Sorted list:', vowels)

print("Python List clear()")
list = [{1, 2}, ('a'), ['1.1', '2.2']]
list.clear()
print('List:', list)

print("Python List max()")
a=[1,2,5,24,62]
print(a)
print(max(a))

print("Python List min()")
a=[1,2,5,24,62]
print(a)
print(max(a))

print("Python List pop(index)")
a=[1,2,5,24,62]
print(a)
print(a.pop(3))
