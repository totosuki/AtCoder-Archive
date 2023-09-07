n = int(input())
a = []
a_2 = []

for i in range(n):
    a.append(input().split())

for i in a:
    a_2.append(int(i[1]))

a_2.index(min(a_2))





