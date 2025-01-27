
def main():
    # Convert decimal 23 to an 8 bit binary number.
    print('{:08b}'.format(23))

    print("Python is cool!")

    # When applying the .3f formatting specifier to the number 76.15854, the result is
    print('{:.3f}'.format(76.15854))

    # What is the decimal equivalent to the binary number 10101010 ?
    print(int('10101010', 2))

    # In Python the ________ symbol is used as the equality operator.
    if(5 == 5):
        print("True")

    # The % symbol is the remainder operator, also known as the ________ operator.
    n = 7
    if(n % 2 == 0):
        print("Even")
    else:
        print("Odd")

    # In Python, the ternary operator is a concise way to write an if-else statement in a single line. 
    # The syntax is:
    print("Even" if n % 2 == 0 else "Odd") 

main()