N, L = map(int, input().split())
S = []
result = ""
for i in range(N):
  S.append(input())
for text in sorted(S):
  result += text
print(result)