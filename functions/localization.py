def pozdrav(ime,jezik="en"):
    lang = {"en":"Hello","rs":"Cao","ru":"Privet"}
    rezultat = (lang[jezik]+" "+ime)
    return rezultat

res = pozdrav("Vlada","rs")
print(res)

