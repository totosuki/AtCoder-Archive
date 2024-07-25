N,M = map(int,input().split())
A = list(map(int,input().split()))
print("Yes" if len([i for i in A if i>=sum(A)/(4*M)])>=M else "No")