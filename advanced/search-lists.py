filmovi = [
    ["Inception","Comedy",["Michael", "Leonardo"]],
    ["Irishman", "Thriller",["Robert de Niro", "Al Pacino"]],
    ["The witcher", "Fantasy",["Henry Cavil"]],
    ["Godfather", "Thriller",["Robert de Niro", "Al Pacino"]],
    ["Bad Grandpa", "Comedy",["Johnny", "Leonardo"]],
    ["The Wolf from Wall Street", "Thriller",["Leonardo"]]
]

#search = "Leonardo"
for film in filmovi:
    #if not search in film[2]:
    #    continue
    print(film[0])
    print("Genre: ",film[1])
    print("Starting: ")
    for glumac in film[2]:
        print(glumac,end=" ")
    print()
