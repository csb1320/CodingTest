n = int(input())

li = list(map(int,input().split()))
#증가하는 수열 - LIS
dp_inc = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            dp_inc[i] = max(dp_inc[i],dp_inc[j]+1)

li.reverse()

#감소하는 수열 - DIS
dp_desc = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            dp_desc[i] = max(dp_desc[i],dp_desc[j]+1)

dp_desc.reverse()

ans = [0 for i in range(n)]

for i in range(n):
    ans[i] = dp_inc[i]+dp_desc[i]

print(max(ans)-1)