N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = "No"

for a in A:
  if a == X:
    answer = "Yes"

print(answer)

# Code Golf
# print(*["Yes"if x in[input().split()]else"No"for n,x in[input().split()]])

# [print("Yes"if x in[input().split()]else"No")for n,x in[input().split()]]

# for n,x in[input().split()]:print("Yes"if x in[input().split()]else"No")

# for n,x in[input().split()]:print("Yes"if x in input().split()else"No")

# for n,x in input().split():print("Yes"if x in input().split()else"No")

# for n,x in input().split():print("NYoe s"[x in input().split()::2])

# for x,y in[open(0)]:print("NYoe s"[x.split()[1]in y.split()::2])

# for x,y in[map(str.split,open(0))]:print("NYoe s"[x[1]in y::2])

# print("NYoe s"[input().split()[1]in input().split()::2])