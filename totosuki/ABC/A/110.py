ABC = list(map(int, input().split()))
ABC.sort(reverse=True)
rslt = ABC[0] * 10 + ABC[1] + ABC[2]
print(rslt)