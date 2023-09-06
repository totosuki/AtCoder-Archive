import sys
input = sys.stdin.buffer.readline

N = int(input())
cards =  [1, 2, 3, 4, 5, 6]

for i in range(N%30):
  cards[i%5], cards[i%5+1] = cards[i%5+1], cards[i%5]

print(*cards, sep = "")