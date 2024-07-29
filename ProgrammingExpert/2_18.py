# Sets

x = set()
x = {1, 2, 1, 2, 3, 1, 3, 2}

print(x)

x.add(4)
print(x)

x.remove(3)
print(x)

# x.clear()
# print(x)

# list, dictionary, sets cannot be added to set

x = {1, 2, 3}
y = {1, 3, 4}

z = x.union(y)  # x | y
print(z)

z = y.intersection(x)  # y & x
print(z)

z = x.difference(y)  # x - y, order matters in difference
print(z)

z = x.symmetric_difference(y)  # y ^ x, order doesn't matter
print(z)
'''
x.update(y)  # y added to x
print(x)
print(y)
'''
x.difference_update(y)
print(x)

x.symmetric_difference_update(y)
print(x)
print(y)

x = {1, 2, 3}
y = {1, 2, 3, 4, 5, 6}

print(x.issubset(y))  # x <= y
print(y.issuperset(x))  # y >= x

x = [1, 2, 3, 4, 2, 1, 2, 5, 4]
z = set(x)
print(type(z))
print(z)

numbers = set()

while True:
  num = int(input("Number: "))

  if num in numbers:
    break

  numbers.add(num)

print(x)
print(y)
print(z)
  