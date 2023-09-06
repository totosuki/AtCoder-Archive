S = input()
N = int(input())
for _ in range(N):
  l, r = map(int, input().split())
  l, r = map(lambda x: x-1, [l,r])
  S = S[:l] + S[l:r+1][::-1] + S[r+1:]
print(S)