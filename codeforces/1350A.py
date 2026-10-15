for _ in range(int(input())):
    n,k=map(int,input().split())
    d=next(i for i in range(2,n+1) if n%i==0)
    print(n+d+2*(k-1))
