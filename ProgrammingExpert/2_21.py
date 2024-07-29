# Mutability - Changable

print(5) 

x = [2]
y = x
x.append(y)
print(x, y)  # here 2 variables are storing the same value

print(x is y)  # tells if 2 objects are the same

a = 1
b = a
print(a is b)

a += 1
print(a is b)

# id() - memory address location of an object

a = 1
b = 1

print(id(a), id(b))

x = []
def func(lst, x):
  lst.append(x)
  print(lst)

a = []
func(a, 2)

print(a)

d = {}
d["k"] = {"v"}

a = d
a["a"] = "b"

print(d, a)
print(d is a)

s1 = set()
s2 = s1

s1.add(1)
s2.add(2)

print(s1 is s2)
print(s1, s2)

def func(s, x):
  s.add(x)

s1 = set()
func(s1, 1)
print(s1)

a = [1, 2, 3]
b = a[:]  # Copy

print(a is b)

def func(lst):
  lst = lst[:]
  lst.append(4)

x = [1, 2, 3]
func(x)
print(x)

s1 = {1, 2, 3}
s2 = s1.copy()  # Create shallow copy of set and dictionary

s1.add(4)
print(s1, s2)

s1 = {"k" : "v"}
s2 = s1.copy()

s1[2] = "b"
print(s1, s2)

lst = [[1, 2, 3], [3, 4, 5]]
lst[0].append(66)

print(lst)

lst = [1, 2, 3]
d = {1 : lst}

lst.append(4)
print(d)

# Mutable objects stored inside immutable objects can be changed

a = [1, 2]
b = [3, 4]
tup = (a, b)

a. append(1)
print(tup)

a = [[1, 2, 3]]
b = a[:]

c = a[0]
c.append(4)

print(a, b)
print(a is b)

y = (1, 2, 3)
y += (7, 8)
print(y)