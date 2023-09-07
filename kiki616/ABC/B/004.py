C = []
for i in range(4):
    c = []
    D = ""
    for l in input():
        c.insert(0,l)
    for i in c:
        D = D + i
    C.insert(0,D)
for i in C:
    print(i)