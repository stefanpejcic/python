import random
number      = random.randint(0,100)
user_guess     = int(input("Enter your score: "))
if(user_guess>number):
    print("Congrats! You beat the  high score!")
else:
    print("Our number ih higher!")
print("Highscore: ", number)
