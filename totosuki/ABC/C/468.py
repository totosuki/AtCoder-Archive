from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
cnt = 0

for arr in permutations(range(1, N+1)):
    cnt += P < arr < Q

print(cnt)
