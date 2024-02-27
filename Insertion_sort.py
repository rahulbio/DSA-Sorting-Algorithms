def insertionsort(customlist):
    for i in range(1,len(customlist)):
        key=customlist[i]
        j=i-1
        while j>=0 and key<customlist[j]:
            customlist[j+1]=customlist[j]
            j-=1
        customlist[j+1]=key
    return customlist

list1=[2,34,334,4,44,43]
print(insertionsort(list1))
        