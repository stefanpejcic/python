user_age = int(input("Input your age: "))

if user_age >= 18:
    print("Your age: ", user_age)
    print("Access granted!")
elif user_age < 18:
    print("Your age: ", user_age)
    print("Access denied!")
else:
    print("please add your age!")
