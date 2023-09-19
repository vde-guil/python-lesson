CHAR_DICT = {
    0: ' ',
    1: '*'
}

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]


# for line in picture:
#     line_to_draw = ""
#     for pixel in line:
#         line_to_draw+=CHAR_DICT[pixel]
#     print(line_to_draw)

# print()

def show_tree():
    for line in picture:
        for pixel in line:
            print(CHAR_DICT[pixel], end="")
        print()

for i in range(2):
    show_tree()
    print()