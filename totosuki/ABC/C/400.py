N = int(input())
A = [2]
# ans = set()
cnt = 0

while A[-1] <= 10**18:
    A.append(A[-1]*2)

for i, a in enumerate(A[:2]):
    if a > N: continue

    mx = N // a
    left = 0
    right = 10**18

    # print(f"a: {a}, mx: {mx}")

    while right - left > 1:
        mid = (left + right) // 2
        # print(f"mid: {mid}, a * mid**2 : {a * mid**2}")

        if mid**2 > mx:
            right = mid
        else:
            left = mid
    
    # print(f"right: {right}")
    
    cnt += left

print(cnt)

# b: 1 4 9 16 25 36
# a: 2 4 8 16 32 64

# a=2: 2 8 18 32 50 72
# a=4: 4 16 36 64 100
# a=8: 8 32 72
# a=16: 16 64
