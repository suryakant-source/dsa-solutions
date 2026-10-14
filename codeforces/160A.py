n=int(input())
a=sorted(map(int,input().split()),reverse=True)
t=sum(a);s=0
for i,v in enumerate(a):
    s+=v
    if s>t-s:
        print(i+1);break
