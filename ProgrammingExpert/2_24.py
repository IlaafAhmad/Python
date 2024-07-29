# Sorting

lst = [2, 1, 3, 4, 5, 2, 3]
lst.sort()  # This modifies the exisitng list
print(lst.sort())  # Gives None
print(lst)

lst = [2, 1, 3, 4, 5, 2]
print(sorted(lst))  # This doesn't modify the existing list
print(lst)

lst.sort(reverse=True)
print(lst)

print(sorted(lst, reverse=True))
print(lst)

def sort_second_index(item):
  return item[1]

lst = [[1, 2], [3, -9], [5, 6], [1, -2]]
lst.sort(key=sort_second_index)
print(lst)  # This sorts by second item

# The end part was confusing. Watch it again