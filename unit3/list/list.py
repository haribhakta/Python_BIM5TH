# features of list
# ordered collection
# supports different data type
# mutable (we can change the elements of list)

# example
mix=["ram",5.2,"bharatpur",40]
# indexing
print(mix[0])
# negative index
print(mix[-2])
# mutable
mix[0]="Shyam"
print(mix)
# slicing
# syntax: list(start:end:step)
print(mix[1:3])
print(mix[:3])
print(mix[2:])
print(mix[:3])
print("slicing = ",mix[::2])

# adding and removing items in list
mix.extend(["data again",34,3.78])
del mix[1]
print(mix)

a = len(mix)
for i in range(a):
    print(mix[i])

a=0
b=len(mix)
while a<b:
    print(mix[a])
    a=a+1

my_list = [1, 2, 3, 4, 5]
squares = [x for x in my_list if x % 2 == 1]
print(squares)

my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
new_list1=list(my_list)
print(new_list1)

# join list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list = list1 + list2
# list1.extend(list2)
for item in list2:
    list1.append(item)
print("Join = ",list1)
