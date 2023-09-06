N = int(input())
a = list(map(int, input().split()))
a.sort()
print(abs(a[0] - a[-1]))