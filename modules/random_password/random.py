from random_password import random_password

#generate random password
random_password()

#generate random password of a specific lenght
random_password(length=16)

#generate random password from given characters
random_password(characters='hello world')

#generate random password of a specific lenght from given characters
random_password(length=4, characters=['hello', 'there', 'my', 'world'])
