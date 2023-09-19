# Dictionary == data type and data structure

# dictionnary = {
#     'weapons': [1,2,3],
#     'greeting': 'hello',
#     'is_magic': True,
#     123: "doesitwork?",
#     True: 'hello',
#     # [100]: True #! can't do it, not hashable, not immutable
# }


# mylist = [
#     {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True
#     },
#     {
#         'a': [4,5,6],
#         'b': 'goodbye',
#         'x': False
#     }
# ]
# print( 'c' in dictionnary)
# print(dictionnary['a'][2])

#############################
### Dictionnaries methods ###
#############################

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

user2 = dict(name='JohnJohn')

print(user.get('age', 55))
print(user2)

print('basket' in  user)
print('size' in  user)

print('age' in user.keys())
print('hello' in user.values())
print( user.items())

# user.clear()
# print(user)

user2 = user.copy()

print(user)
print("popping age off")
print(user.pop('age'))
print(user)

print(user.popitem()) ## remove a random pair in dict

print(user.update({'age': 55}))
print(user)