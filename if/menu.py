SHOW_PRODUCT = 1
BUY_PRODUCT  = 2
EXIT_PROGRAM  = 3


PRODUCT_NAME  = "iPhone"
PRODUCT_PRICE = 699

User_Balance  = int(input("Enter balance: "))
User_Command  = int(input("Enter command: "))

if(User_Command == 1):
    print("Product name: ", PRODUCT_NAME)
    print("Product Price: ", PRODUCT_PRICE)
if(User_Command == 2):
    if User_Balance >= PRODUCT_PRICE:
        print("You bought an ", PRODUCT_NAME)
    if User_Balance < PRODUCT_PRICE:
        print("You don't have enough balance.")
if(User_Command == 3):
    print("Good bye!")
    


    
