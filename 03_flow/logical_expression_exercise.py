is_magician = True
is_expert = False

# check if magician and expert: " you are a master magician"

# if magician but not expert: " at least you're getting there"


# if not magician: "You need magic powers"

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician:
    print("at least you're getting there")
elif is_expert:
    print("You need magic powers")

print(True == 1) # true
print('' == 1) #false
print([] == 1) # false
print(10 == 10.0) # true
print([1, 2, 'a'] == [1, 2, 'a']) # false

list1 = [1, 2, 3]
list2 = list1



# print(list1 == list2)