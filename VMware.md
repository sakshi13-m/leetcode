# Find the second smallest number with sum of digits equals to N and number of digits equal to d.
## constraint 
* N>=2 
* d>=2 

Here's my python solution 
```
s,digit=map(int,input().split())
t=[0 for i in range(digit)]
s-=1
for i in range(digit-1,0,-1):
    if(s>9):
        t[i]=9
        s-=9
    else:
        t[i]=s
        s=0
t[0]=s+1
f1,f2=0,0
for i in range(digit-1,-1,-1):
    if(f1==0 and t[i]>0):
        t[i]-=1
        f1=1
    elif(f1==1 and f2==0 and t[i]<9 ):
        t[i]+=1
        f2=1
print(''.join(str(i) for i in t))

```
## Sample test case
### input - 20 3  
### output - 398 
### input - 2 5 
### output - 10010

