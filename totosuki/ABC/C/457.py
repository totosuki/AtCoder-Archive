N, K = map(int, input().split())
L = []
A = []
alen = []
for _ in range(N):
    l, *a = map(int, input().split())
    L.append(l)
    A.append(a)
    alen.append(len(a))
C = list(map(int, input().split()))
now = 0
cnt = 0
while True:
    cnt += C[now] * alen[now]
    if cnt >= K:
        before = cnt - C[now] * alen[now]
        print(A[now][(K - before - 1) % alen[now]])
        exit()
    now += 1
