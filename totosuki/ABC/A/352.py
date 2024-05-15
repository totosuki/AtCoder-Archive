N, X, Y, Z = map(int, input().split())
ans = "No"
if X <= Z <= Y or Y <= Z <= X:
    ans = "Yes"
print(ans)