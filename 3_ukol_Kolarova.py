import json

with open('body.json', encoding = 'utf-8') as file:
    text = json.load(file)
print(text)

result = {}
for key in text:
    score = text[key]
    if score >= 60:
        result[key] = "Pass"
    else:
        result[key] = "Fail"

text.update(result)
print(text)

with open('prospech.json', mode='w', encoding='utf=8') as file:
    json.dump(text, file, ensure_ascii=False)