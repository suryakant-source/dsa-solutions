n=int(input())
x=0
for _ in range(n):
    t=input()
    x+=1 if '+' in t else -1
print(x)
