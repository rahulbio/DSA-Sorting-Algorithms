import math
def insertionsort(customlist):
    for i in range(1,len(customlist)):
        key=customlist[i]
        j=i-1
        while j>=0 and key<customlist[j]:
            customlist[j+1]=customlist[j]
            j-=1
        customlist[j+1]=key
    return customlist



def bucketsort(customlist):
    no_of_buckets=round(math.sqrt(len(customlist)))
    maxv=max(customlist)
    arr1=[]
    for i in range(no_of_buckets):
        arr1.append([])
    for j in customlist:
        index_b=math.ceil((j*no_of_buckets)/maxv)
        arr1[index_b-1].append(j)
    
    for i in range(no_of_buckets):
        arr1[i]=insertionsort(arr1[i])
    
    k=0
    for i in range(no_of_buckets):
        for j in range(len(arr1[i])):
            customlist[k]=arr1[i][j]
            k+=1
    return customlist

list1=[1,2,45,32,12,45,23,12]
print(bucketsort(list1))
