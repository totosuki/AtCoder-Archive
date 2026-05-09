N, K = map(int, input().split())
A = list(map(int, input().split()))


def check(X) -> bool:
    cnt = 0
    for i in range(N):
        if A[i] >= X:
            continue
        cnt += ((X - A[i]) + (i + 1) - 1) // (i + 1)
        if cnt > K:
            return False
    return True


left = 1
right = 10**18 * 2 + 1000
while right - left > 1:
    mid = (right + left) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
