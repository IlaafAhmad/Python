# Lists

lst = [1, 2, 3, True, "hello"]
print(lst)
print(lst[2])
print(lst[-1])

lst[2] = 55  # changes list element
print(lst)

lst.append(5)  # extends and add new element

print(len(lst))

lst.pop(3)  # pop last element

count = lst.count(2)  # count how many times it occurs
print(count)

index = lst.index(1)  # first time element occurs
print(index)

remove = lst.remove(55)  # remove first occurence of an element
print(lst)

list_contains_5 = 5 in lst
print(list_contains_5)

x = [1, 2, 3]
y = [1, 2]
combined = x + y
print(combined)
combined[2] = 66
print(combined)

x.extend(y)
print(x)
print(y)

lst1 = [[5, 6, [100]], [2, 3], [1, 2, 3]]
print(lst1[0][-1][0])
