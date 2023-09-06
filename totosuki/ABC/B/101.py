N = input()
SN = 0
for i in range(len(N)):
  SN += int(N[i])

print("Yes") if int(N) % SN == 0 else print("No")