'''
Create a simple python calculator with the most basic operations: add,sub,mul,div
Ask a user for two numbers and an operation, than print the result.
'''



first     = int(input("Input first operand: "))
second    = int(input("Input second operand: "))
operation = input("Operation (add,sub,mul,div): ")

if operation == "add":
    print ("Result is: ", first + second)
elif operation == "sub":
    print ("Result is: ", first - second)
elif operation == "div":
    print ("Result is: ", first % second)
elif operation == "mul":
    print ("Result is: ", first * second)
else:
    print("Unknown operation")
