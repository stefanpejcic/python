import os,time
w = 30
h = 10
px = 4
py = 3

stepx = 1
stepy = 1

while True:
    os.system("cls")
    px+=stepx 
    py+=0.1
    for y in range(h):
        for x in range(w): 
            if px >= w-1:
                stepx=-1
            if px <= 0:
                stepx=1
            if y == int(py) and x == px:
                print("@",end="")
            else:
                print(" ",end="")
        print()
    time.sleep(1/60) 
