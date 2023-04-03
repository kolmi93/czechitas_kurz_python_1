name_surname = input("Napiště své jméno a příjmení.\n")

print(name_surname.upper())

print(name_surname.lower())

list = name_surname.split(" ")
name = list[0]
surname = list [-1]
name_1 = name[0]
name_2 = name[1:]
surname_1 = surname[0]
surname_2 = surname[1:]
print(name_1.upper() + name_2.lower() + " " + surname_1.upper() + surname_2.lower())
# varianta č.2:
print(name_surname.title())

print(name_1.upper () + "." + surname_1.upper() + ".")

if len(name)>5:
    name_3 = (name[0])
    print(name_3.upper() + "." + surname.title())
else:
    print(name_1.upper() + name_2.lower() + " " + surname.title())