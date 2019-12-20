import time,os
sprite  = "#"
bound   = 50
x       = 1
d       = 1
  
while True:
    print("\r",end="")
    for n in range(bound):
        print(sprite if n==x else " ",end="")
    time.sleep(0.016)
    x+=d
    if x<=0 or x>=bound-1: 
        d*=-1
