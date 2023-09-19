def is_even(num):
    return num % 2 == 0

def highest_even(li):
    high_even = None

    for num in li:
        if high_even is None:
            high_even = num
        
        high_even = num if is_even(num) \
            and num > high_even else high_even
    
    return high_even



print(highest_even([10, 2, 3, 4, 8, 11, 67, 32, 99]))