s=input()
a=s.lower()
print(a)
for i in a:
    if a.count(i)==1:
        print(i,end=" ")
    
