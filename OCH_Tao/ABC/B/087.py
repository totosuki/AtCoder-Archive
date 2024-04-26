A = int(input())
B = int(input())
C = int(input())
X = int(input())
l = []
for i in range(A+1):
  for j in range(B+1):
    for k in range(C+1):
      l.append(500*i+100*j+50*k)
print(len([i for i in l if i==X]))