# N,X = map(int,input().split())
# A = list(map(int,input().split()))
# print("Yes" if X in A else "No")
print(*["Yes"if x in[input().split()]else"No"for n,x in[input().split()]])