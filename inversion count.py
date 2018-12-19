#list1=[1,4,6,3,2,5,7,9,8,0]
#list1=[0,2,4,5,7,1,3,6,7,8,9]
#list1=[1, 3, 5, 6, 7, 8, 9]
#list1=[3,1]
#list1=['a','c','d','t','z','n','o','p']
#list1=[1,3,5,2,4,6,15,14,13,12,11,10,7,9,8]
#test
#count=0
#for i in range(len(list1)):
#    for j in range(i+1,len(list1)):
#        if list1[i]>list1[j]:
#            count+=1       
#print('result: ',count)




list1=[]
f = open("data.txt", "r")
for line in f:
    list1.append(int(line.strip()))
print('done reading input')



inversion=0
def merge_sort(list1,inversion):
    
    if len(list1)==1:
        return list1,inversion
    m=len(list1)//2
    
    list11=list1[0:m]
    list12=list1[m:len(list1)]
    

    list11,inversion1=merge_sort(list11,inversion)
    list12,inversion2=merge_sort(list12,inversion)
    
    inversion+=inversion1+inversion2    
    for iii in range(len(list11)):
        for jjj in range(len(list12)):
            if list11[iii]>list12[jjj]:
                inversion+=1
    
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
                #inversion+=1
        elif j==len(list11) and k<len(list12):
                list1_sorted.append(list12[k])
                k=min(k+1,len(list12))
        elif k==len(list12) and j<len(list11):
                list1_sorted.append(list11[j])
                j=min(j+1,len(list11))
                #inversion+=1
    
    return list1_sorted, inversion 
list_sorted, inversion=merge_sort(list1,inversion)
print('Inversion=',inversion)            
        
  