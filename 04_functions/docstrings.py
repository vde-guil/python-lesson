def test(a):
    '''
    Info: this function tests and prints param
    '''
    print(a)

test("caca")
# help(test)

# print(test.__doc__)

# clean code
def is_odd_or_even(num):
    return num % 2 == 0


print(f"is 50 even? : {is_odd_or_even(51)}")

# *args and **kwargs

def super_func(*args, **kwargs):

    return  sum(args) + sum(kwargs.values())

print(super_func(1, 2, 3,  4, 5, num1=5, num2=90))


lst = [1, 2, 3, 4, 5]

# Rule: params, *args, default parameters, **kwargs