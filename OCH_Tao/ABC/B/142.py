N,K = map(int,input().split())
H = list(map(int,input().split()))
print(len([i for i in H if i>=K]))