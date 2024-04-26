L1,R1,L2,R2 = map(int,input().split())
R = set(range(L1,R1+1))
B = set(range(L2,R2+1))
print(max(len(R&B)-1,0))