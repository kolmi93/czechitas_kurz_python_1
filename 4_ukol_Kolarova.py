phone_number = input("Na jaké telefonní číslo chcete zpávu odeslat?\n")

def phone_verification(phone_number):
    if len(phone_number) == 9:
        print("true")
    elif len(phone_number) == 13 and phone_number[0:4] == ("+420"):
        print("true")
    else:
        print("false")

phone_verification(phone_number)

message = input("Jakou zprávu chcete poslat?\n")

def message_price(message):
    if len(message) == 0:
        price = 0
        print(f"Cena Vaší zprávy je: {price} Kč.")
    elif len(message) >= 1 and len(message) <= 180:
        price = 3
        print(f"Cena Vaší zprávy je: {price} Kč.")
    elif (len(message)/180) == 0:
        price = len(message)//180
        print(f"Cena Vaší zprávy je: {price} Kč.")
    else:
        price = (len(message)//180 + 1)
        print(f"Cena Vaší zprávy je: {price} Kč.")

message_price(message)