# Misc. Python Syntax

# Comprehension - Initializing a data structure or data type in one line

lst = [i for i in range(1, 10)]
print(lst)

lst = [i / 2 for i in range(1, 11) if i % 2 == 0]
print(lst)

lst = [i * j for i in range(1, 11) for j in range(5)]
print(lst)

# With tuples, you will get a generator

s = {i * j for i in range(1, 11) for j in range(5)}  # For sets
print(s)

dic = {i: j for i in range(3) for j in range(10)}
print(dic)

# Multiple Assignments - Multiple variables to one or multiple values

x = y = z = 1
print(x, y, z)

# Unpacking - Taking iterable objects like tuple or list and unpacking it into individual values.

x, y = 2, 3  # This is (2, 3) tuple
print(x, y)



def foo():  # Docstring is a comment that goes at the top of the function
  """
  this is the foo function
  """
  pass

# help(foo)  # help tells what the documentation is
# help(len)

help(max)
