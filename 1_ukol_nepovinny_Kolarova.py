name_surname = input("Napiště své jméno a příjmení.\n")

print(name_surname.upper())

print(name_surname.lower())

list = name_surname.split(" ")
name = str(list[0])
surname = str(list [-1])
name_1 = name[0]
name_2 = name[1:]
surname_1 = surname[0]
surname_2 = surname[1:]
print(str(name_1.upper() + name_2.lower() + " " + surname_1.upper() + surname_2.lower()))

print(name_1.upper () + "." + surname[0] + ".")

if len(name)>=5:
    name_3 = str(name[0])
    print(name_3.upper() + "." + surname_1.upper() + surname_2.lower())
else:
    print(name_1.upper() + name_2.lower() + " " + surname_1.upper() + surname_2.lower())