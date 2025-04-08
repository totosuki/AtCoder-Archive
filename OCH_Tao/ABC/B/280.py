from numpy import diff
N = int(input())
S = list(map(int,input().split()))
print(S[0],*diff(S),sep=" ")