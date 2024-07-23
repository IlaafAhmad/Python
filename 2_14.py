'''
for i in range(-5, 5, 2):
  print(i)

result = 0

for i in range(1, 11):
  result += i  # result + i

print(result)

lst = [1, 2, 3, True, False]
for idx in range(len(lst)):
  print(lst[idx])

for element in lst:
  print(element)

for i, element in enumerate(lst):
  print(i, element)

for i in range(0, len(lst), 2):
  print(i)


lst1 = [1, 2, 3, 4, 5, 4, 4, 5, 2]

for num in lst1:
  if num == 4:
    break
  print(num) 

for num in lst1:
  if num == 4:
    continue

  print(num)

st = "hello world!"

for i, char in enumerate(st):
  if char == "w":
    print(i)
'''
numbers = []
for i in range(4):
  num = int(input("Enter a number: "))
  numbers.append(num)
print(numbers)
