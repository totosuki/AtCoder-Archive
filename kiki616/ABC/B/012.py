N = int(input())
h,m,s = 00,00,00
h = N // (60*60) 
m = N % (60*60) // 60
s = N % (60*60) % 60
a = [h,m,s]
for i in range(3):
    if a[i] < 9:
        a[i] = f"0{a[i]}"

print(f'{a[0]}:{a[1]}:{a[2]}')