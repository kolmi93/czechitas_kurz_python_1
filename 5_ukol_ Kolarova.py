teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#průměr teplot pro kadý den
day = [sum(day)/len(day) for day in teploty]
print(day)

# seznam ranních teplot
morning = [temperatures[0] for temperatures in teploty]
print(morning)

# seznam nočních teplot
evening = [temperatures[3] for temperatures in teploty]
print(evening)

# seznam dvouprvkovýh seznamů poledních a nočních teplot
noon_evening_2 = [[temperatures[1], temperatures[-1]] for temperatures in teploty]
print(noon_evening_2)