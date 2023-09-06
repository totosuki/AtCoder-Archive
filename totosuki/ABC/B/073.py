N = int(input())
answer = 0
for _ in range(N):
  l, r = map(int, input().split())
  answer += r - l +1
print(answer)