_ = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
turn = 0
alice = []
bob = []

for n in a:
  turn += 1
  if turn % 2 == 1:
    alice.append(n)
  else:
    bob.append(n)

print(sum(alice) - sum(bob))