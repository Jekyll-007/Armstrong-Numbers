def is_armstrong_number(num):
    digits = str(num)
    power = len(digits)
    sum_of_power = sum(input("Enter a number: "))

user_input = int(input("Enter a number: "))

if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")