## Calculator


def calc(x, y):
    add = x + y
    subtract = x - y 
    multiply = x * y
    divide = x / y
    print("Add: {} Subtract: {}  Multiply: {} Divide: {}".format(add, subtract, multiply, divide))
     



# Ask for first value

fValue = input("Enter the first value to evaluate: ")

# Ask for second value
sValue = input("Enter the second value to evaluate: ")

calc(int(fValue), int(sValue))
