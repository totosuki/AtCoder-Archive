n = int(input())
a = list(map(int,input().split()))
count = 0
point = True

while point:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i]/2
        else:
            point = False
    count += 1
count -= 1
print(count)

# n = int(input())
# a = list(map(int,list(input().split())))
# count = None

# while sum(map(lambda an:an % 2 == 0,a)) == n:
#     count =+ 1
#     map(lambda u:u/2,a)
#     if map(lambda l:l ==0,a):
#         break

# if a[0] % 2 == 0 :
#     count =+ 1    

# print(count)

