class text_colors:
    MAGENTA = '\033[95m'
    BLUE= '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
 
def getMode():
    while True:
        print("please chose the following ")#print on screen
        print (text_colors.GREEN + "\n ENCRYPT or e" + text_colors.ENDC)
        print (text_colors.RED + "\n DECRYPT or d" + text_colors.ENDC)
        print (text_colors.YELLOW + "\n BRUTEFORCE or b\n\n" + text_colors.ENDC)
        mode = input(">")#allows user to input a value on screen
        print (text_colors.BLUE + "\nyou selected %s" % mode + text_colors.ENDC) #reply what you typed
        #if mode in "encrypt e decrypt d".split():
        return mode # retunr the value of mode
       
 
 
 
 
 

def getMessage():#function for the message
    print ("\nEnter your message here:")
    message = input("\n>")
    print (text_colors.BLUE + "\nyou selected %s" % message + text_colors.ENDC)
    return message #retunr message
 
 

def getKey(): # function for the key
    key = 0 # key is set to the value of zero
    while True:#keeps looping intill a value has been entered
        print("enter the key number (%d)" % (26)) # asking to enter a key number value
        key = int(input("\n>")) #raw input for the user to insert a number
        if (key >= 1 and key <= 26): #if whats entered is greater than 1 and less then 26
           print (text_colors.BLUE + "\nyou selected %d" % key + text_colors.ENDC)
        return key#return key value
 
 
 

def getTranslatedMessage(mode,message,key):
    if mode[0] == "d":#checks if first letter in string is d for decrypt
        key = -key  # makes key a negavctie value for decryption
    translated = '' #declaring translated
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
           
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
 
            translated += chr(num)
        else:
 
            translated += chr(num)
    return translated

 
mode = getMode() # looks back to mode to do the brute force
message = getMessage() #message is getmessage
if mode[0] != "b": #if mode is brute force
    key = getKey() #get all the keys from 1 - 26
 
print ("your translated text is")
if mode[0] != "b":#
    print (text_colors.BLUE + (getTranslatedMessage(mode, message, key)) + text_colors.ENDC)
else:
    for key in range(1, 26 + 1):
        print (key, getTranslatedMessage("decrypt", message, key))
 
 
message = getMessage()
key = getKey()
 
print (text_colors.BLUE + "\nyour secret message is :" + text_colors.ENDC)
print (getTranslatedMessage(mode, message, key))
