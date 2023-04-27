teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

keys = [day[0] for day in teploty]
values = [sum(day[1:]) / len(day[1:]) for day in teploty]
new_dict = dict(zip(keys, values))
print(new_dict)

#podle zadání z github
new_dict_2 = ({den[0]: sum(den[1:]) / len(den[1:]) for den in teploty})
print(new_dict_2)