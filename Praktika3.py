import json

with open('users.txt') as file:
    users = [user.strip() for user in file.readlines()]
    res = []
    for item in users:
        name, age, gender = item.split('|')
        res.append({'name': name, 'age': int(age), 'gender': gender})
    with open('users.json', 'w') as file1:
        json.dump(res, file1)
