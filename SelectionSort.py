def selectionsort(list1):
    for i in range(len(list1)):
        min_index=i
        for j in range(i+1,len(list1)):
            if list1[min_index]>list1[j]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i] 
    return list1

list_test=[1,2,4,3,21,12]
print(selectionsort(list_test))