"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    input_string = input("Enter an Operator and Number(s): ")
    input_string = input_string.split(' ')
    if input_string[0] == "q":
        break
    else:
        pass

