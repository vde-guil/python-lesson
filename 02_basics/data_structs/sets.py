## set ##
#########

# unordered collection of unique elements

# my_set = {1,  3, 2, 4, 5, 5}
# my_set.add(100)
# my_set.add(2)

# print(my_set)


# my_list = [1,  3, 2, 4, 5, 5]

# my_set = set(my_list)

# print(my_set)
# # print(my_set[0]) #! can't do that, more like a dict

# print(1 in my_set)
# print(len(my_set))

# new_set = my_set.copy()
# my_set.clear()

# print(my_set)
# print(new_set)

my_set = { 4, 5}
your_set = { 4, 5, 6, 7, 8, 9, 10}

# difference()
# discard()
# difference_update()
# intersection()
# isdisjoint()
# issubset()
# issuperset()
# union()

# print(my_set.difference(your_set))

# print(my_set.discard(5)) # remove in place
# print(my_set)

# my_set.difference_update(your_set) # remove in place
# print(my_set)

# print(my_set.intersection(your_set))
# print(my_set & your_set)


# print(my_set.isdisjoint(your_set))

# print(my_set.union(your_set))
# print(my_set | your_set)

print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))