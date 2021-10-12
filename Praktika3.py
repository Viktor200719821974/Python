import json

with open('users.txt', 'r') as file:
    content = file.read()
    fileLine = content.splitlines()
    d = []
    for i in fileLine:
        l = i.split('|')
        d.append(l)
        x = iter(['name', 'age', 'gender'])
        y = iter(d)
        k = zip(x, y)
        print(k)


    #     # print(d)
    #     b = {}
    #     for j in l:
    #
    #         y = i
    #     b.update(dict.fromkeys(x, y))
    # print(b)
    # items = []
    # for line in file:
    #     if not line.strip():
    #         continue
    #     d = {}
    #     x = ['name', 'age', 'gender']
    #
    #     data = line.split('|')
    #     for val in data:
    #         d = dict.fromkeys(x, val)
    #         for key in x:
    #             key, sep, value = val.partition(':')
    #             d[key.strip()] = value.strip()
    #
    #     items.append(d)
    #     print(items)
    # i = iter(["a", "a", "b", "c", "b"])
    # j = iter([1, 2, 3, 4, 5, 6, 7, 8])
    # k = list(zip(i, j))
    # print(k)
    # d = {}
    # for (x, y) in k:
    #     if x in d:
    #         d[x] = d[x] + y
    #     else:
    #          d[x] = y
