import random

number_to_guess = random.randint(0, 256)
print('''
Can you guess the number?
            
''')

while True:
    input_number = int(input("Please enter a number: "))
    if input_number > number_to_guess:
        print("It's less")
    elif input_number < number_to_guess:
        print("It's more")
    else:
        break

print(f"Congratulation! you've guessed. The number was {number_to_guess}")
