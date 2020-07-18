"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    input_string = input("Enter an Operator and Number(s): ")
    input_string = input_string.split(' ')
    operator= input_string[0]


    if operator == "q":
        break
    else:
        num1= int(input_string[1])
        if len(input_string) ==3:
            num2= int(input_string[2])

  

    
            

