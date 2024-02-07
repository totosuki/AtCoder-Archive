A,B,X = map(int,input().split())
print(B//X-A//X+1 if A%X==0 else B//X-A//X)