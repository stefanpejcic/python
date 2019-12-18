x = int(input("Input number: "))

i = 1
print('1\t2\t3')

for i in range(1,x+1):
    for j in range(1,x+1):
        print(i*j,end="\t")
    print()
