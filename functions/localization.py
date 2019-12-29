def greeting(name,language="en"):
    lang = {"en":"Hello","rs":"Cao","ru":"Privet"}
    local = (lang[language]+" "+name)
    return local

res = greeting("Vlada","rs")
print(res)

