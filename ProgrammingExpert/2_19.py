# Handling and Raising Exceptions

try:
  int("hello")
except:
  print("Exception")

try:
  # 2 / 0
  int("hello")
except ValueError as e:
  print("Exception", e)
except ZeroDivisonError as e:
  print("Zero Exception", e)

# For all kinds of exceptions -

try:
  2 / 0
except Exception as e:
  print("Exception", e)
finally:  # Always run and is used to clean up
  print("Done")

# raise ValueError("This is an error!")

# raise Exception("This is an exception!")

num = input("Enter a number:")

if not num.isdigit():
  raise ValueError("This is not a valid number>")

while True:
  num = input("Enter a number: ")

  try:
    num = float(num)
    break
  except ValueError as e:
    print("Not a valid float, try again!", e)