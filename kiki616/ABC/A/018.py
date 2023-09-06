
array = []
for i in range(3):
    array.append(int(input()))
for i in array:
    print(sorted(array,reverse=True).index(i)+1)