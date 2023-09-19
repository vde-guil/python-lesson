############
## Tuple  ##
############

my_tuple2 = ( 1, 2, 3, 4, 5)
# my_tuple[1] = 'z' #! won't work, immutable

print(my_tuple2[1])
print(5 in my_tuple2)

user = {
    (1, 2): [1,2,3],
    'greet': 'hello',
    'age': '20'
}

print((1, 2) in user)

my_tuple = (1, 2, 3, 4, 5, 5, 5)
new_tuple = my_tuple[1:3]
print(new_tuple)

(x, y, *rest) = my_tuple
print(my_tuple.count(5))

print(my_tuple.index(5))
print(len(my_tuple))