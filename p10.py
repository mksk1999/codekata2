s=input()
b=[]
b.append(s[0])
for i in range(1,len(s)):
    if(i%3==0):
        b.append(s[i])
for i in b:
    print(i,end="")
    
