# Conditionals

'''
number = float(input("Enter a number below: "))
if number < 5:
  print("good job")
elif number >= 6:
  print("number is above 5")
else:
  print("not a good job")

'''

number = float(input("Enter a number: "))

if number > 0 and number % 2 == 0:
  print("This a positive even number")
  number2 = float(input("Number:"))
  if number2 < 0:
    print("This is a negative number")
  else:
    print("This is a positive")
else:
  print("Number")


# if statement in one line

x = 5
result = "Ok" if x > 5 else "Not ok"
print(result)

