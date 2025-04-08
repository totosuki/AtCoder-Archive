L,R = map(int,input().split())
S = list(input())
S[L-1:R]=reversed(S[L-1:R])
print(*S,sep="")