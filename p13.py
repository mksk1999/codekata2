s=input()
c=0
d=0
for i in s:
    if(i=='('):
        c+=1
    else:
        d+=1
if(c==d):
    print("yes")
else:
    print("no")
