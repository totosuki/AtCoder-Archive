N = int(input())
P = [int(input()) for _ in range(N)]
P.sort()
rslt = sum(P[:-1]) + P[-1]//2
print(rslt)