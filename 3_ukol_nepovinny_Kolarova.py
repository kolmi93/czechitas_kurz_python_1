import json

with open('body.json', encoding = 'utf-8') as file:
    students_list = json.load(file)

with open('bonusy.json', encoding = 'utf-8') as file_2:
    bonuses = json.load(file_2)

def merge_dict(students_list, bonuses):
    new_dict = {**students_list, **bonuses}
    for key, value in new_dict.items():
        if key in students_list and key in bonuses:
            new_dict[key] = [value, (students_list[key] + bonuses[key])]
    return new_dict

new_dict = merge_dict(students_list, bonuses)
print(new_dict)