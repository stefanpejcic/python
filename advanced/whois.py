import whois

data = input("Enter a domain: ")
w = whois.whois(data)

print (w)
