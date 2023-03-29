x,y,z=map(int, input().split())
 
if x%z==0:
    a=x//z
else:
    a=x//z + 1
    
if y%z==0:
    b=y//z
else:
    b=y//z + 1
    
print(a*b)