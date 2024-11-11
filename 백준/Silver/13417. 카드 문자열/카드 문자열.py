import sys
from collections import deque


T = int(input())

for i in range(T):
    n = int(input())
    card = deque(map(str, sys.stdin.readline().split()))
    result = deque()
    result.append(card.popleft())
    while card:
        if card[0] <= result[0]:
            result.appendleft(card.popleft())
        else:
            result.append(card.popleft())
    print(''.join(result))
