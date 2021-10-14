import json

with open('users.txt', 'r') as file:
    content = file.read()
    fileLine = content.splitlines()
    d = []
    for i in fileLine:
        l = i.split('|')
        d.append(l)

f = [x for xs in d for x in xs]

d = []
a = ['name', 'age', 'gender']
b = a * int(len(f) / len(a))
k = dict(zip(b, f))
with open('my_file.json', 'w') as file:
    json.dump(k, file)
