N,M=map(int,input().split())
s=set(range(1,M+1))
for i in range(N):s=s&set(map(int,input().split()[1:]))
print(len(s))