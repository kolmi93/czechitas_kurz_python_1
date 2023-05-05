import re

user_name = input("Zadejte Vaše uživatelské jméno:\n")
regular_string_1 = re.compile(r"[A-Za-z]{6,10}")
print(regular_string_1.fullmatch(user_name))

password = input("Zadejte heslo:\n")
regular_string_2 = re.compile(r"(\w[- \. \+ =]{12,30})")
print(regular_string_2.fullmatch(password))

email = input("Zadejte Váš e-mail:\n")
regular_string_3 = re.compile(r"\"?[A-Za-z0-9_]+\+*\-?\.?[A-Za-z0-9_]+\"?@[A-Za-z0-9]+\-?[A-Za-z0-9]*[.][A-Za-z0-9]*[[com,net,museum,name,jp,co,cz]{1}\.?[net,museum,name,com,jp,co,cz]?")
print(regular_string_3.fullmatch(email))