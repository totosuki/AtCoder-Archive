N = int(input())
X = list(map(int, input().split()))
ans = "Yes"

for x in X:
    if x >= 0:
        ans = "No"

print(ans)