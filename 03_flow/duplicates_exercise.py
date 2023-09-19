some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'd', 'd', 'd']

res = {}

# for elem in some_list:
#     res[elem] = 1 if elem not in res else res[elem]+1


# for key, count in res.items():
#     if count > 1:
#         print(key)


# while len(some_list):
#     curr_char = some_list.pop(0)
    
#     curr_char_index = []
#     for i, elem in enumerate(some_list):
#         if curr_char == elem:
#             curr_char_index = [i] + curr_char_index

#     if len(curr_char_index):
#         print(f"{curr_char} appears {len(curr_char_index) + 1} times")

#     for pos in curr_char_index:
#         some_list.pop(pos)

duplicates = []

for i, value in enumerate(some_list):
    if (value in some_list[i + 1:]) and not (value in duplicates):
        duplicates.append(value)

print(duplicates)

