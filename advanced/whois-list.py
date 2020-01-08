import whois
domeni = ["wporb.com","pluginsbay.com","pcelarstvopejcic.com","hostipay.com","filmovic.com","oklagije.com","giga.rs"]
for domen in domeni:
    w = whois.whois(domeni[0])
    print(domeni[0], w.expiration_date)
print()
