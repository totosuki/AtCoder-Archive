A,B = map(int,input().split())
l = []
l.append(A+B)
l.append(A-B)
l.append(A*B)
print(max(l))