'''
Create a simple script that asks users to input their age, than print their age and grant/resctrict access if they are 18+
'''

user_age = int(input("Input your age: "))

if user_age >= 18:
    print("Your age: ", user_age)
    print("Access granted!")
elif user_age < 18:
    print("Your age: ", user_age)
    print("Access denied!")
else:
    print("please add your age!")
