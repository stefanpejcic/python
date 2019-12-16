'''
Get a random number from 1-10, then let user take a guess to gt a higher number.
'''

import random
number      = random.randint(0,10)
user_guess     = int(input("Enter your score: "))
if(user_guess>number):
    print("Congrats! You beat the  high score!")
else:
    print("Our number ih higher!")
print("Highscore: ", number)
