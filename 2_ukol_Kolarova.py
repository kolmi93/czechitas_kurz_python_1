sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

pozadavek = input("Jakou součástku potřebujete koupit?\n")
if pozadavek in sklad:
    print ("Vámi požadovaná součástka je skladem.")
    mnozstvi = int(input("Jaké množství potřebujete nakoupit?\n"))
    for sklad, amount in sklad.items():
        if mnozstvi > amount:
            print("Lze dodat pouze omezené množství kusů.")
        else:
            print("Poptávku lze uspokojit v plné výši.")
else:
    print("Vámi požadovaná součástka není skladem.")
    exit()