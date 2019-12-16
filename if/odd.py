match = input('Enter match? ')
odd1 = input("Enter tip for home: ")
if(not odd1.replace(".","").isnumeric()): 
    print("Sorry home tip is not numeric")
    exit(0)
if(float(odd1)<=1):
    print("Odd cannot be less than one")
    exit(0)
odd2 = input("Enter tip for draw: ")
if(not odd2.replace(".","").isnumeric()):
    print("Sorry draw tip is not numeric")
    exit(0)
if(float(odd2)<=1):
    print("Odd cannot be less than one")
    exit(0)
odd3 = input("Enter tip for away: ")
if(not odd3.replace(".","").isnumeric()):
    print("Sorry your tip is not numeric")
    exit(0) 
if(float(odd3)<=1):
    print("Odd cannot be less than one")
    exit(0)

print("Thank you, your odd is: ")
print("Match: ", match)
print("Home: ", odd1)
print("Draw: ", odd2)
print("Away: ", odd3)

