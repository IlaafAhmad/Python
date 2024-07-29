# Strings

s = "Ilaaf Ahmad"
print(s[4])
print(len(s))

# s.count
# s.find() , -1 if it doesn't exist

upper = s.upper()
lower = s.lower()
capitalize = s.capitalize()
print(upper)
print(lower)
print(capitalize)

str = "19"
is_digit = str.isdigit()  # check for integer
print(is_digit)

l = "hello, my name"
words = l.split(",")
print(words)

l1 = l.replace(",", "|")
print(l1)

print(f"Hello, {1 - 2}, Ilaaf, {9 * 3}")

string = """Hello my name is string 
111 """
print(string)

sss = f'{9*2}\'s'  # \ 
print(sss)

lst = ["il", "a", "af"]
strs = "-".join(lst)
print(strs)