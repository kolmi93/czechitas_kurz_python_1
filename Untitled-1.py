name_surname = input("Napiště své jméno a příjmení.\n")
if len(name)>5:
    name_3 = (name[0])
    print(name_3.upper() + "." + surname_1.upper() + surname_2.lower())
else:
    print(name_1.upper() + name_2.lower() + " " + surname_1.upper() + surname_2.lower())