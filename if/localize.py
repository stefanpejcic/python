"""
Get language input from a user, then greet him in that language.
"""

language = input("Language: ")

if language == "rs":
    print("Zdravo!")
elif language == "de":
    print("Hallo!")
elif language == "en":
    print("Hello!")
elif language == "pl":
    print("Witaj!")
else:
    print("Sorry, we don't support your language yet.")
    print("Help us translate our website to your language: hello@localize.com")
