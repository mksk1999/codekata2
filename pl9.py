s=input()
b=[]
for i in s:
    if(i>='A' and i<='Z'):
        b.append(chr(ord(i)+32))
    else:
        b.append(chr(ord(i)-32))
for i in b:
    print(i,end="")
