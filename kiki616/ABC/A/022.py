N,S,T = map(int, input().split())
W = int(input())
cnt = 0
if S <= W and W <= T:
    cnt = cnt + 1
for i in range(N - 1):
    A = int(input())
    W = W + A
    if S <= W and W <= T:
        cnt = cnt + 1
print(cnt)