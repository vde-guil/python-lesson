# Fundamental Data Types
int
float
bool
str
list
tuple
set
dict

# Classes -> custom types

# Specialized Data Types (modules loaded from libraries/packages)

# Unique Data Type
None

##################

## Fundamental Data Types

# numbers:

# integers

type(2)
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)

print(2 ** 3)
print(5 // 4)
print(5 % 4)

# math functions
print(round(3.9))
print(abs(-25))

## Operator precedence

20 + 3 * 4

# bin -> binary

print(str(bin(5))[2:])

# variables

iq = 190
print(iq)

# expression vs statement

iq = 100
res = iq / 4

# statement = whole line
# expression processes something (calculation etc...) eg  'iq / 4' is an expression

# augmented assigment operator

some_value = 5
some_value = some_value + 2
some_value += 2
some_value -= 4

# strings

print(type("hi hello there!"))
username = 'supercoder'
password = 'super\
secret'
long_string = '''
WOW
0 0
---
'''

print(long_string)
first_name = 'Andrei'
last_name = 'Neagoie'
full_name = first_name +  " " + last_name
print(full_name)

# string concatenation

print("hello", 5)
print('hello' + ' Andei' + str(5))

print(type(str(100)))

# formatted strings

name = "Johnny"
age = 55

print("hi " + name + ". you are " + str(age) +" years old")
print("hi {0}.  you are {1} years old".format(name, age)) # old way
print(f"hi {name}.  you are {age} years old") # new way

#string indexes

selfish = 'me me me'

# [start:stop:stepover] => string slicing
#                        
print(selfish[0:8:2])

print(selfish[::-1])

selfish = "l" + selfish[1:]
print(selfish)

# builtin function and methods

quote = 'to be or not to be'

print(quote.upper())
print(quote.replace("be", "suck"))

print(bool('False'))