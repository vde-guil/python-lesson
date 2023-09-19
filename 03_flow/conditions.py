# Conditionnal logic

is_old = True
is_licenced = True

if is_old and is_licenced:
    print('you are old enough to drive and you have a licence!')

else:
    print("you're either too young or unlicenced to drive...")

print("this will be executed anyway")

print(bool('  '.strip()))

# ternary Operator

# condition_if_true if condition else condition_if_false

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

# short circuiting

is_friend = True
is_user = True

if is_friend or is_user:
    print('best friends forever')

# logical operator
# >, <, <=, >=, ==, !=, and, or, not, is