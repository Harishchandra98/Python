def add(a):
    ans = int(a[0])+int(a[1])
    print(ans)

f=open("cal.txt","r")

for i in f:
    a=i.split()
    add(a)

f.close()    
    



