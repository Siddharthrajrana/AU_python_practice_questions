def find_smaller_number(num1, num2):
    if num1 < num2:
        raise AssertionError("First number is smaller")
    else:
        return min(num1, num2)


print(find_smaller_number(12,4))
