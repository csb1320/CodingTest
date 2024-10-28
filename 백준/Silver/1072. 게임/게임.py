x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
    exit()

start = 1
end = 1000000000
result = -1

while start <= end:
    mid = (start + end) // 2
    if (y + mid) * 100 // (x + mid) > z:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
