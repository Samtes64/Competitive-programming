s=str(input())
arr=[]

for i in s:
    if i>="a" and i<="z":
        if i not in arr:
            arr.append(i)
print(len(arr))