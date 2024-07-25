N,X,Y,Z = map(int,input().split())
print("Yes" if Z in range(min(X,Y),max(X,Y)+1) else "No")