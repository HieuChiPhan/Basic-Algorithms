#list1=[1,4,6,3,2,5,7,9,8,0]
#list1=[0,2,4,5,7,1,3,6,7,8,9]
#list1=[1, 3,5, 6, 7, 8, 9]
#list1=[1, 3]
#list1=['a','c','d','t','z','n','o','p']
list1=[1,3,5,2,4,6]
print('input: ',list1)
def merge_sort(list1):
    if len(list1)==1:
        return list1
    m=len(list1)//2
    
    list11=list1[0:m]
    list12=list1[m:len(list1)]
    
    list11=merge_sort(list11)
    list12=merge_sort(list12)
    
    list1_sorted=[]
    j=0
    k=0

    for i in range(len(list1)):
        if j<len(list11) and k<len(list12):
            if list11[j]<=list12[k]:
                list1_sorted.append(list11[j])            
                j=min(j+1,len(list11))                             
            elif list11[j]>list12[k]:
                list1_sorted.append(list12[k])
                k=min(k+1,len(list12)) 
        elif j==len(list11) and k<len(list12):
                list1_sorted.append(list12[k])
                k=min(k+1,len(list12))
        elif k==len(list12) and j<len(list11):
                list1_sorted.append(list11[j])
                j=min(j+1,len(list11))                
    return list1_sorted 
print('output:',merge_sort(list1))            
        
   