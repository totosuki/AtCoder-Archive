[print(l[1]) if l[1] < (min(D) + l[2]) else print(min(D) + l[2]) for l in [list(map(int, input().split()))] for D in [list(map(int, input().split()))]]

N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
D.sort()

print(P) if P < (D[0] + Q) else print(D[0] + Q)