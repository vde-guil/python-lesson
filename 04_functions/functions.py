# parameters
# positionnal arguments
def say_hello(name, emoji):
    print(f"helloo {name}{emoji}")


# arguments
say_hello("Valentin", "=D") # call/invoke
say_hello("Emily", ";D")
say_hello("Dan", "=>")

# keyword arguments
say_hello(emoji=':S', name="Antonin") # bad practice

# default parameters

def say_something(name='Darth Vader', emoji='8|'):
    print(f"helloo {name}{emoji}")

say_something()

# Return

def my_sum_generator(addend):
    def another_func(num):
                return addend + num
    return another_func


add_two = my_sum_generator(2)


print(add_two(5))

##################

def some_random_stuff():
    pass
