import json

with open('body.json', encoding = 'utf-8') as file:
    students_list = json.load(file)

with open('bonusy.json', encoding = 'utf-8') as file_2:
    bonusy = json.load(file_2)

def Merge(students_list, bonusy):
    return(students_list.update(bonusy))

print(Merge(students_list, bonusy))