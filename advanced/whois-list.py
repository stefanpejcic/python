import whois
domeni = ["wporb.com","pluginsbay.com","pcelarstvopejcic.com","hostipay.com","filmovic.com","oklagije.com","giga.rs"]
while True:
    for domen in domeni:
        w = whois.whois(domen)
        print(domen, w.expiration_date)
print()
