sum = 0

while True:
    userInput = input("Enter number: ")
    if userInput == "":
        print("Total result:",sum)
    else:
        if userInput.isnumeric():
            sum+=int(userInput)
        else:
            print("Value is not numeric")
