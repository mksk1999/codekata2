n=int(input())
l=list(map(str,input().split()[:n]))
l.sort()
l.sort(key=len)
for i in l:
    print(i,end=" ")
    
    

