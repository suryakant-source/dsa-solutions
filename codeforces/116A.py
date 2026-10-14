n=int(input())
c=m=0
for _ in range(n):
    a,b=map(int,input().split())
    c+=b-a
    m=max(m,c)
print(m)
