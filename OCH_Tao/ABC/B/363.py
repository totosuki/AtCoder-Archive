N,T,P = map(int,input().split())
L = list(map(int,input().split()))
L.sort(reverse=True)
print(max(0,T-L[P-1]))