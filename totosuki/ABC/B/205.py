import sys
input = sys.stdin.buffer.readline

N = int(input())
len_A = len(set(map(int, input().split())))

print("Yes") if N == len_A else print("No")