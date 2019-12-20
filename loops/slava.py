import time
datum = 1
slava = 19

for dan in range(1,32):
    if dan == slava:
        print("Srecna slava domacine!!!")
    else:
        doslave = slava - dan
        print("Srecan",doslave,"dan do slave")
    time.sleep(0.1)
