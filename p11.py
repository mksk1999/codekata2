import math
l,r=map(int,input().split())
c=0
for i in range(l,r+1):
    s=math.sqrt(i)
    if(math.sqrt(i)==int(s)):
        c+=1
print(c)
    
