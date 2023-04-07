x,y=map(int, input().split())
count=0
for i in range(x):
    i,j=map(str, input().split())
    if i=="+":
        y+=int(j)
    else:
        if int(j)<=y:
            y-=int(j)
        else:
            count+=1
print(y,count)


