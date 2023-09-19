# scope - what variable do i have access to

def some_func():
    total = 100

# print(total) #! error, total is in some_fun scope

# a = 1

# def confusion():
#     global a
#     a += 5
#     return a

# print(confusion())
# print(a)

# b = 10

# def parent():
#     b = 25
#     def confusion():
#         return b + 5
#     return confusion()

# print(parent())
# print(b)


def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()

    print("outer:", x)

outer()