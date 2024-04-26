N,L = map(int,input().split())
print(sum(sorted(list(range(L,L+N)),key=abs)[1:]))