#list1=[1,4,6,3,2,5,7,9,8,0]
list1=[0,2,4,5,7,1,3,7,6,8,9]
#list1=[1, 3, 5, 6, 7, 8, 9]
#list1=[3,1]
#list1=['a','c','d','t','z','n','o','p']
#list1=[1,3,5,2,4,6,15,14,13,12,11,10,7,9,8]
print(list1)
def quick_sort(list1): #with duplicate
    if len(list1)<=1:
        return list1
    # pivot picking rule
    pivot=len(list1)//2
    list11=[]
    list12=[]
    duplicate=0
    for i in range(len(list1)):
        if list1[pivot]>list1[i]:
           list11.append(list1[i])
        elif list1[pivot]<list1[i]:
           list12.append(list1[i])
        elif list1[pivot]==list1[i]:
            duplicate+=1
#    print(list11)
    list11=quick_sort(list11)
    list12=quick_sort(list12)
    if duplicate==0:
        list1=list11+[list1[pivot]]+list12
    else:
        list1=list11+[list1[pivot]]*duplicate+list12
    return list1

print(quick_sort(list1))


# for no duplication
#def quick_sort(list1): #without duplicate
#    if len(list1)<=1:
#        return list1
#    # pivot picking rule
#    pivot=len(list1)//2
#    list11=[]
#    list12=[]
#    for i in range(len(list1)):
#        if list1[pivot]>list1[i]:
#           list11.append(list1[i])
#        elif list1[pivot]<list1[i]:
#           list12.append(list1[i])
#    list11=quick_sort(list11)
#    list12=quick_sort(list12)
#    list1=list11+[list1[pivot]]+list12
#    return list1
#
#print(quick_sort(list1))