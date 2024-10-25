def is_armstrong_number(num):
    digits = str(num)
    power = len(digits)
    sum_of_power = sum(int(digit) ** power for digit in digits)
    return sum_of_power == num

user_input = int(input("Enter a number: "))

if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")