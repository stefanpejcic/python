while True:

    command = input("Input number: ")

    if command == "exit":
        print("Die!")
        break

    x = int(command)
    for j in range(1,x+1):
        print(j,end="\t")
    print() 
    i = 1

    for i in range(1,x+1):
        for j in range(1,x+1):
            print(i*j,end="\t")
        print()
