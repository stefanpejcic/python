'''
Grade users performance: Ask them for a number from 1-5 and than print a small description about the grade.
'''

grade = int(input('Grade: '))
if(grade==1):
    print("Worse")
elif(grade==2):
    print("Bad")
elif(grade==3):
    print("Average")
elif(grade==4):
    print("Good")
elif(grade==5):
    print("Excellent")
else:
    print("you call that grade?")
