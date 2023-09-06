import math
N = int(input())
A = list(map(int, input().split()))
A = [a for a in A if a != 0]
print(math.ceil(sum(A) / len(A)))