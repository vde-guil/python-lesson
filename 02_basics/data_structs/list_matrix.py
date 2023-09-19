li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', 'b', True]


# Data Structure
# way to organise info and data into a box, with different pros and cons
# container around data with different way of access, organize...

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]


# List slicing

print(amazon_cart[0::2])

# strings are immutable

greet = 'hello'
#! greet[0] = 'z'  immutability => not allowed


amazon_cart[0] = 'laptop'
print(amazon_cart[1:3])
print(amazon_cart)

# list slicing create a new list

new_cart = amazon_cart[1:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# matrix

matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9],
]

matrix[0][0]

# lists methods

basket = [1,2,3,4,5]

# adding

new_list = basket.append(100)
print(f"new list = {new_list}")

print(basket)
print(len(basket))

basket.insert(4, 20)
print(basket)

# extend

basket.extend([101, 102, 103])
print(basket)

# remove

item = basket.pop()
print(basket)
print(item)

basket.pop(0)
print(basket)

basket.remove(102)
print(basket)

basket.clear()
print(basket)

####

basket = ['a', 'x', 'b','c','d','e', 'b']


print('d' in basket) # True
print('i' in 'hi my name is Ryan') # False

print(basket.count('b'))

# Sort

print(basket.sort()) # SORT IN PLACE

print(sorted(basket)) # CREATE A NEW SORTED LIST

print(basket)

# reverse
basket.reverse()
print(basket)

# TIPS AND TRICKS FOR LISTS

print(len(basket))

# reverse trick
print(basket[::-1])

# generate list quickly

generated_list = list(range(1,101))

# JOIN

sentence = " "

joined_sentence = sentence.join(["hi", "my", "name", "is", "Jojo"])
print(joined_sentence)

# List unpacking

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

a,b,c, *other, d = my_list

print(a, b, c)
print(other)
print(d)

# None

weapons = None
print(weapons)