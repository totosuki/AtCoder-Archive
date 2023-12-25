A,B,C = map(int,input().split())
l = []
l.append(A+B)
l.append(B+C)
l.append(C+A)
l.sort()
print(l[0])