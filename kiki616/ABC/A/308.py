
array = list(map(int,input().split()))

for i in range(1,8):
    
    if array[i-1] <= array[i] and array[i] % 25 == 0:
        pass
    else:
        array.append(676)

if array[0] >= 100 and array[7] <= 675 and len(array) == 8:
    print("Yes")
else:
    print("No")