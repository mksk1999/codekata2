n,k=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in m:
    l.append(i)
    print(max(l),end=" ")
