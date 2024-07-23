x = 0
while x < 5:
  x += 1
  print(x)

num = input("Enter an integer: ")

while not num.isdigit():
  num = input("Enter an integer: ")

while True:
  num = input("Enter an integer: ")
  if num.isdigit():
    break

lst = [2, 3, 3, 4, 2, 1]

result = 0
i = 0
while result < 9 and i < len(lst):
  result += lst[i]
  i += 1
  print(lst[i])

# while else