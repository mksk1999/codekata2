n=int(input())
b=[]
for i in range(1,n+1):
    if(n%i==0):
        b.append(i)
for i in b:
    if(i%2==0):
        print(i,end=" ")
