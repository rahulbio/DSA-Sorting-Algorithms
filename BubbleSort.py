def bubblesort(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1

test_list=[1,2,3,5,4]
print(bubblesort(test_list))