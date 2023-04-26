import json

with open('body.json', encoding = 'utf-8') as file:
    students_list = json.load(file) 

with open('bonusy.json', encoding = 'utf-8') as file_2:
    bonuses = json.load(file_2)

new_dict = {}
for key in students_list:
    new_dict[key] = students_list[key] + bonuses.get(key, 0)
for key in bonuses:
    if key not in new_dict:
        new_dict[key] = bonuses[key]

marks = {}
for key in new_dict:
    score = new_dict[key]
    if score >= 90:
        marks[key] = 1
    elif score >= 70 and score <= 89:
        marks[key] = 2
    elif score >= 50 and score <= 69:
        marks[key] = 3
    elif score >= 30 and score <= 49:
        marks[key] = 4
    else:
        marks[key] = 5
print(marks)

with open('znamky.json', mode='w', encoding='utf=8') as file:
    json.dump(marks, file, ensure_ascii=False)