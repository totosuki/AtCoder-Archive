import sys
input = sys.stdin.buffer.readline

print(len(bin(int(input())[3:])))

# AC
# k = 0

# while True:
#   if 2**k > N:
#     break
#   k += 1

# print(k - 1)