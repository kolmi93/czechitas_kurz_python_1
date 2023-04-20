import json
with open('body.json', encoding='utf-8') as file:
    text = file.read()

print(text)
result = {}
for key in text:
    score = text[key]
    if score >= 60:
       result[key] = "Pass"
    else:
       result[key] = "Fail"
text.update(result)

with open('body.json', mode='w', encoding='utf-8') as file:
   json.dump(result, file)

