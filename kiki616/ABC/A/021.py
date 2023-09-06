N = int(input())
A = int()
a = 0
if N % 2 == 0:
    A = N / 2
else:
    A = (N - 1) / 2
    a = 1
print(int(A+a))
for i in range(int(A)):
    print(2)
if a == 1:
    print(1)