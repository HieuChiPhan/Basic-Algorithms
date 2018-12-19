import random

dict1=dict()
f = open("data.txt", "r")
for line in f:
    words=line.strip().split()
#    words=[int(x) for x in words]
    dict1[words[0]]=words[1:]    
#print(dict1)

def delete_self_loop(dict1):
    for key in dict1:
            for val in dict1[key]:
                if key in dict1[key]:
                    dict1[key].remove(key)
    return dict1
#
def random_choose_link(dict1):
    key_list=list(dict1.keys())
    node_i=random.choice(key_list)
    node_j=random.choice(dict1[node_i])
    return node_i,node_j


def change_network(dict1,removed_link):
    list_i=dict1[removed_link[0]]
    list_j=dict1[removed_link[1]]
    list_i_delete=[]
    list_j_delete=[]
    for i in list_i:
        if i!=removed_link[1]:
            list_i_delete.append(i)
    for i in list_j:
        if i!=removed_link[0]:
            list_j_delete.append(i)
#    print('list_i',list_i)
#    print('list_i_delete',list_i_delete)
    list_i=list_i_delete
    list_j=list_j_delete        
#    list_i.remove(removed_link[1])
#    list_j.remove(removed_link[0])
    list_ij=list_i+list_j
    dict1[removed_link[0]]=list_ij
    
#    del dict1[removed_link[1]]
#    for key in dict1:
#            for val in dict1[key]:
#                newkey=[]
#                if val==removed_link[1]:
##                    print('============')
##                    print(val,dict1[key])
#                    dict1[key].remove(val)
#                    dict1[key].append(removed_link[0])
    del dict1[removed_link[1]]
    for key in dict1:
            newlist=[]
            for val in dict1[key]:               
                if val!=removed_link[1]:
                   newlist.append(val)
                elif val==removed_link[1]:
                    newlist.append(removed_link[0])
#            print(newlist)
            dict1[key]=newlist

    return dict1




def contraction (dict1):
    dict1=delete_self_loop(dict1)
    while len(dict1)>2:
        removed_link=random_choose_link(dict1)
#        print(removed_link)
        dict1=change_network(dict1,removed_link)
        dict1=delete_self_loop(dict1)
    return dict1
leng_cuts=[]
for i in range(10):
    print(i)
    dict2=dict1.copy()
    dict2=contraction (dict2)
    key_list2=list(dict2.keys())
    leng_cuts.append(len(dict2[key_list2[0]]))

print(leng_cuts)

print('minimum_cut=',min(leng_cuts))


