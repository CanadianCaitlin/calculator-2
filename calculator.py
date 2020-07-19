"""CLI application for a prefix-notation calculator."""
from arithmetic import (add, subtract, multiply, divide, square, cube,
                       power, mod)


def calculator2():
    while True:
        input_string = input("Enter an Operator and Number(s): ")
        input_string = input_string.split(' ')
        operator= input_string[0]

        if operator == "q":
            break
        else:

            num1= float(input_string[1])
            if len(input_string) ==3:
                num2= float(input_string[2])

            #add
            if operator == "+":
                print(num1+num2)
            #substract
            elif operator == "-":
                print(num1-num2)
            #multiply
            elif operator == "*":
                print(num1*num2)
            #divide
            elif operator == "/":
                print(num1/num2)
            #cube
            elif operator == "cube":
                print(num1**3)
            #power
            elif operator == "pow":
                print(num1**num2)
            #mod
            elif operator == "mod":
                print(num1 % num2)
            #square
            elif operator == "square":
                print(num1**2)
            
calculator2()
        

        

  

    
            

