n=int(input())
s=list(map(int,input().split()))
result=[1]*n

for i in range(n):
    for j in range(i):
        if(s[i]<s[j]):
            result[i]=max(result[i],result[j]+1)

print(max(result))