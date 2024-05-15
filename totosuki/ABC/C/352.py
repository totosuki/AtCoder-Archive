m,*A=0,
j,*B=0,
for i in range(int(input())):
 a,b=map(int,input().split());A+=[a];B+=[b]
 if m<b-a:m=a-b;j=i
a=0
for i in range(len(A)):
 if i!=m:a+=A[i]
print(a+B[j])