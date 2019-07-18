l=list(map(str,input().split()))
c=0
for i in range(len(l[0])):
    if(l[0][i]!=l[1][i]):
        c+=1
b=int(l[2])
if(c==b):
    print("yes")
else:
    print("no")
