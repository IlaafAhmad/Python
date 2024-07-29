# Functions

def print_value():
  print("hello")

print_value()

def print_value(value):
  print(value)

print_value("hi")
print_value(1)

def add_5(x, y):
  result = x + y + 5
  print(result)

add_5(5, 7)

x = 4
y = 5

add_5(x, y)

def multiply(x, y, z):
  result = x * y * z
  return result
  print("hi")  # This doesn't get printed
x = 5
y = 6
z = 3

r = multiply(x, y, z)
print(r)

# Anything put after a return statement is not executed since programs ends

def new_range(start=0, stop=10):
  x = start

  while x < stop:
    print(x)
    x +=1

new_range(stop=5, start=-5)

def return_values(x, y):
  return x + 1, y + 1

result = return_values(1, 2)
print(result)

x, y = return_values(1, 2)
print(x, y)

def remove_chars(base, chars):
  new_string = base
  for char in chars:
    new_string = new_string.replace(char, "")

  return new_string

result = remove_chars("Hello world", "l")
print(result)

def sum_lists(list1, list2):
  list1_sum = sum_list(list1)
  list2_sum = sum_list(list2)
  return list1_sum, list2_sum

def sum_list(lst):
  total = 0

  for num in lst:
    total += num

  return total

sum1, sum2 = sum_lists([1, 2, 3, 4], [2, 3, -7, 2])

print(sum1, sum2)
