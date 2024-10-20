def is_palindrome(number):
    return str(number) == str(number)[::-1]

def count_digits(number):
    digit_count = [0] * 10
    while number:
        digit_count[number % 10] += 1
        number //= 10
    return digit_count

try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Please enter a non-negative number.")
    elif is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
        for digit, count in enumerate(count_digits(num)):
            if count:
                print(f"Digit {digit} appears {count} times.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
