N = int(input())
A = list(map(int, input().split()))
ans = [0]*N
cnt = 0

for i in range(len(A)):
    if i-A[i] >= 0:
        ans[i-A[i]] += 1


for i in range(len(A)):
    if i+A[i] < N:
        cnt += ans[i+A[i]]

print(cnt)