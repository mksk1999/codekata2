s=input()
b=[]
for i in s:
    if(i>='0' and i<='9'):
        b.append(i)
if(len(b)==len(s)):
    print("yes")
else:
    print("no")
