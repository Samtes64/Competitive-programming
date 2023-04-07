number=int(input())
ans=[]
x = [int(x) for x in input().split()]
y = sorted(x)
i=int(input())
for j in range(i):
    a,b,c=map(int, input().split())
    num=0
    if a==1:
        
        for t in range(b-1,c):
            num+=x[t]
    
    
    else:
        for t in range(b-1,c):
            num+=y[t]    
    ans.append(num)

for val in ans:
    print (val)   