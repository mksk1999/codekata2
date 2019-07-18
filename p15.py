s=input()
a=s.replace(' ','')
print(a)
for i in a:
    if(i>='a' and i<='z'):
        if a.count(i)==1:
            print(i,end=" ")
    else:
        if a.count(i)==1:
            print(i,end=" ")
    
    
 
