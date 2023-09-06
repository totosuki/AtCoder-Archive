ABC = list(map(int, input().split()))
K = int(input())
ABC.sort()

rslt = ABC[0] + ABC[1] + ABC[2] * (2 ** K)

print(rslt)