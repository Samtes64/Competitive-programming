x=int(input())
while x>0:
    max=0
    bulbs=input()
    for i in range(4):
        if bulbs.count(bulbs[i])>max:
            max=bulbs.count(bulbs[i])
    if max==4:
        print(-1)
    elif max==1 or max==2:
        print(4)
    elif max==3:
        print(6)
    x-=1