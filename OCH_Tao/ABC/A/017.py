N1 = list(map(int, input().split()))
N2 = list(map(int, input().split()))
N3 = list(map(int, input().split()))
score = 0
score += int(N1[0] * N1[1] / 10)
score += int(N2[0] * N2[1] / 10)
score += int(N3[0] * N3[1] / 10)
print(score)