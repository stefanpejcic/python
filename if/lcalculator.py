phrase1 = "Enter first operand? "
phrase2 = "Enter second operand? "
phrase3 = "Choose operation (add,sub,mul,div): "
phrase4 = "Result is: "
phrase5 = "Unknown operation"

lang = input('Choose language (sr,en,de): ')

if(lang=="sr"):
    phrase1 = "Unesite prvi broj? "
    phrase2 = "Unesite drugi broj? "
    phrase3 = "Odaberite operaciju (add,sub,mul,div): "
    phrase4 = "Rezultat je: "
    phrase5 = "Nepoznata operacija"
elif(lang=="en"):
    phrase1 = "Enter first operand? "
    phrase2 = "Enter second operand? "
    phrase3 = "Choose operation (add,sub,mul,div): "
    phrase4 = "Result is: "
elif(lang=="de"):
    phrase1 = "Geben Sie die erste Nummer ein? "
    phrase2 = "Geben Sie die zweite Nummer ein? "
    phrase3 = "Operation wählen (add,sub,mul,div): "
    phrase4 = "Das Ergebnis ist: "
    phrase5 = "Unbekannte Operation"

a = int(input(phrase1))
b = int(input(phrase2))
op = input(phrase3)

if(op=='add'):
    print(phrase4, a + b) 
elif(op=='sub'):
    print(phrase4, a - b)
elif(op=='mul'):
    print(phrase4, a * b)
elif(op=='div'):
    print(phrase4, a / b)
else:
    print(phrase5)
