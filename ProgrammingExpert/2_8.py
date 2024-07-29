# Conditions

'''
cond1 = 3.0 == 3
print(cond1)

cond2 = 3 != 3
print(cond2)

cond3 = 3 == "5"
print(cond3)  # We can compare strings with other data types only with == or !=
'''

str1 = "Hello"
str2 = "hello"
cond4 = str1 == str2
print(cond4)

str3 = "Ac"
str4 = "ab"
cond5 = str3 < str4
print(cond5)

# ord() - gives ascii value
# chr() - takes ascii value and gives character associated with it
# Ascii value of lowercase is greater than uppercase

print(ord("b"))
print(chr(77))