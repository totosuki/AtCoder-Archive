S = input()
a, b = map(int, input().split())
rslt = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
print(rslt)