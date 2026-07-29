N = int(input())
A = list(map(int, input().split()))
cnt = 0

for i in range(N-2):
    cnt += A[i] < A[i+1] > A[i+2]

print(cnt)