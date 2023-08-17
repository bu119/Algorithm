from collections import deque

n = int(input())
cards = deque(range(1,n+1))
move = []

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
