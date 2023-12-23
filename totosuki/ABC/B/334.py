A, M, L, R = map(int, input().split())

start = (L - A + M - 1) // M
end = (R - A) // M

trees = max(0, end - start + 1)

print(trees)