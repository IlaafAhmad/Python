# Dictionaries

# key -> value
'''
x = {2: "hello", "1": 5}
print(x[2])
print(x)

dic = {}
dic["key"] = "value"
print(dic["key"])

y = dict()  # create dictionary function

z = {1: 1, 2: 2, 3: 3, 4: 5}
del z[1]  # delete a key
print(z)

values = z.values()  # this shows values and not keys
print(values)

keys = z.keys()
print(keys)

items = list(z.items())
print(items)  

# convert all the above to list for finding a specific element
print(items[0])

for key in z:
  value = z[key]
  print(key, value)

for key, value in z.items():
  print(key, value)

z[6] = z.get(6, 3) + 2
print(z)
z[6] = z.get(6, 3) + 2
print(z)
'''

characters = {}

string = "hello world"

for char in string:
  characters[char] = characters.get(char, 0) + 1

print(characters)

counts = {}

while True:
  num = input("Number (enter q to quit): ")

  if num == "q":
    break

  num = int(num)
  counts[num] = counts.get(num, 0) + 1

print(counts)
print(num)