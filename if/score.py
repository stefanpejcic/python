"""
1. create a small quiz with 3 questions and 3 answers
2. give user 1 point for each correct answer
3. Tell them their score at the end
"""

User_Score = 0

question1 = input("Best computer ever? ")
question2 = input("Best game ever? ")
question3 = input("Best movie ever? ")

answer1   = "amiga"
answer2   = "fallout"
answer3   = "matrix"

if(question1 == answer1):
    User_Score +=1 
if(question2 == answer2):
    User_Score +=1 
if(question3 == answer3):
    User_Score +=1 
    
print("Your score: ", User_Score)
