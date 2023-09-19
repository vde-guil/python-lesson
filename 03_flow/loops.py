
for item in 'Zero to Mastery':
    print("{" + item, end="}")
print()
# iterables => means object or collection that can be iterated over
# can be a list, a dictionnary, typle, set, string

 

users = {
    "name": 'Gollum',
    "age": 5006,
    "can_swimm" : False
}

for key, value in users.items():
    print(key, value)

for value in users.values():
    print(value)

for key in users.keys():
    print(key)

# range
# iterate over int

my_sum = 0
for item in range(0, 99):
    my_sum += item


