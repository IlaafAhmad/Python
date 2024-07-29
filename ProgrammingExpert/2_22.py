# Scope - where variables are accessing from

def foo():
  x = 0
  print(x)

foo()
# print(x)  # x inside function is different than x here

x = 1  # This x is different than x inside a function

def loc():
  x = 2
  print(x)

loc()
print(x)

# Anything defined inside a function is not accessible outside of function while anything defined outside of function is accessible inside function

inp = int(input("Enter a number:"))

if inp > 5:
  value = "Greater than 5!"

# print(value)  # Here any value below 5 won't be printed since it is not defined outside so value never gets created

def add_5(x):
  x = x + 5
  print(x)

x = 10
print(x)
add_5(x)

def append_5(x):
  x.append(5)
  print(x)

x = []  # Mutability occurs here
print(x)
append_5(x)
print(x)
print(x)

# Using global is considered bad practice and make it difficult to debug

value = 5
def foo():
  global value  # this modifies value even outside of the function when you call it. 
  value = 10
  print(value)

print(value)  # this is equal to 5
foo()
print(value)  # this changes to 10 since function is called above

