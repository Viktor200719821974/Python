import json

with open('users.txt', 'r') as file:
    content = file.read()
    fileLine = content.splitlines()
    d = []
    for i in fileLine:
        l = i.split('|')
        d.append(l)

f = [x for xs in d for x in xs]

d = {}
a = iter(['name', 'age', 'gender'])
c = iter(f)
k = list(zip(a, c))
for (x, y) in k:
    if x in d:
        d[x] = d[x] + y
    else:
        d[x] = y
print(d)

