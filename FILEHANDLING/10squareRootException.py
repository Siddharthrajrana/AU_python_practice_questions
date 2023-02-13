import math

def find_square_root(number):
    if number < 0:
        raise ValueError("Negative number not supported")
    return math.sqrt(number)

print(find_square_root(4))
