l,k=map(int,input().split())
n=list(map(int,input().split()))
for i in n:
    if(i==k):
        b=1
        break
    else:
        b=2
if(b==1):
    print("Yes")
else:
    print("No")
