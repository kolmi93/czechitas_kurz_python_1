store = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

item = input("Jakou součástku potřebujete koupit?\n")
if item in store:
    print ("Vámi požadovaná součástka je skladem.")
    demand = int(input("Jaké množství potřebujete nakoupit?\n"))
    if demand > store[item]:
        deficit = demand - (store[item])
        print(f"Lze dodat pouze omezené množství kusů. Aktuálně je k dispozici {store[item]} ks. Chybí {deficit} ks.")
        store.pop(item)
    else:
        print("Poptávku lze uspokojit v plné výši.")
        store[item] -= demand
else:
    print("Vámi požadovaná součástka není skladem.")