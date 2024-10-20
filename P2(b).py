def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def octal_to_hexadecimal(octal):
    decimal = 0
    for digit in octal:
        decimal = decimal * 8 + int(digit)

    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal:
        hexadecimal = hex_digits[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal or "0"

# Get user input and print results
binary = input("Enter a binary number: ")
octal = input("Enter an octal number: ")

print(f"Binary {binary} is equal to decimal {binary_to_decimal(binary)}")
print(f"Octal {octal} is equal to hexadecimal {octal_to_hexadecimal(octal)}")
