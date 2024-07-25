# Math

x = abs(-9)  # gives absolute value meaning positive value  
print(x)

print(abs(-29.5))

x = max(1, 2, 5)
print(x)

y = max("a", "c", "k")
print(y)

x = min(-2, -5, 5, 1)
print(x)

x = sum([1, 2, 3, 8, 4])  # only works on iterable objects meaning lists, set, dictionaries and tuples where we can store more than one value
#  x = sum(1, 2, 3, 4)  # This will be invalid
print(sum)

x = round(4.50)
print(x)

x = round(2.82734024, 3)  # This will round to 3 values
print(x)

import math  # Always write packages that you need to import at the top of program. Not here

x = math.sin(90)  # This is in radian not degrees
print(x)

x = math.cos(0)
print(x)

x = math.cos(math.pi)
print(x)

import random

random_number = random.randint(1, 10)
print(random_number)

random_odd_number = random.randrange(1, 10, 2)
print(random_odd_number)

lst = ["he", "hi", "hello", "hey"]
random_str = random.choice(lst)
print(random_str)
