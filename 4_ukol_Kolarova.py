import math

phone_number = input("Na jaké telefonní číslo chcete zpávu odeslat?\n")

phone_standart = phone_number.replace(" ", "")

def phone_verification(phone_standart):
    if len(phone_standart) == 9:
        return True
    elif len(phone_standart) == 13 and phone_standart[0:4] == ("+420"):
        return True
    else:
        return False
    
phone_verification(phone_standart)

if phone_verification(phone_standart) == True:
    message = input("Jakou zprávu chcete poslat?\n")
else:
    print("Napsali jste špatný formát telefonního čísla. Prosím, zkuste to znovu.")
    exit()

def message_price(message):
    lenght = math.ceil((len(message)/180))
    price = (lenght*3)
    print(f"Cena Vaší zprávy je: {price} Kč.")

message_price(message)