import sys
input = sys.stdin.readline

count = 8
n = int(input())

i = 1
while True:
    if n - (2**i) == 0:
        count = count + i + 2
        break
    elif n - (2**i) < 0:
        count = count + i + 1
        break

    i += 1

print(count)