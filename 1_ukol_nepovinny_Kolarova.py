name_surname = input("Napiště své jméno a příjmení.\n")

print(name_surname.upper())

print(name_surname.lower())

jmena = name_surname.split(" ")
jmena.upper([0][0])
jmena.lower([0][1:])
jmena.upper([1][0])
jmena.lower([1][1:])
print(jmena.upper([0][0]) + jmena.lower([0][1:]) +" " + jmena.upper([1][0]) + jmena.lower([1][1:]))
