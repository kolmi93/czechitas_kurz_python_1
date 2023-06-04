import math

phone_number = input("Na jaké telefonní číslo chcete zpávu odeslat?\n")

phone_standart = phone_number.replace(" ", "")

def phone_verification(phone_standart):
    if len(phone_standart) == 9:
        return True
    elif len(phone_standart) == 13 and phone_standart[:4] == ("+420"):
        return True
    return False

if phone_verification(phone_standart):
    message = input("Jakou zprávu chcete poslat?\n")
else:
    print("Napsali jste špatný formát telefonního čísla. Prosím, zkuste to znovu.")
    is_valid = False

    while not is_valid:
        new_number = input("Na jaké telefonní číslo chcete zprávu odeslat?\n")
        if len(new_number) == 9 or (len(new_number) == 13 and new_number[:4] == ("+420")):
            is_valid = True
            message = input("Jakou zprávu chcete poslat?\n")
            break
        else:
            is_valid = False
            print("Napsali jste špatný formát telefonního čísla. Prosím, zkuste to znovu.")

def message_price(message):
    lenght = math.ceil((len(message)/180))
    price = (lenght*3)
    print(f"Cena Vaší zprávy je: {price} Kč.")

message_price(message)