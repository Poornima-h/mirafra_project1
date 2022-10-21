try:
    n=int(input())
    a=map(int,input().split())
    m=min(a)
    print(-1,[2*sum(a)])
except Exception as e:
    print(e)