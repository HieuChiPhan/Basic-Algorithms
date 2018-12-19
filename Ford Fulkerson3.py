
n=6 #Number of nodes
V=list(range(n)) #node ID
S=0 #source
T=n-1 #tank
#E=[[0,1],[1,3],[0,3],[1,2],[3,4],[2,3],[2,4],[2,5],[4,5]] #link
#C=[16,4,5,12,20,9,7,5,20] #Capacity =21

#E=[[0,1],[1,3],[0,3],[3,2],[3,4],[4,2],[2,5],[4,5],[1,2]] #link
#C=[9,10,9,1,3,8,10,7,8] #Capacity =12

#E=[[0,1],[1,3],[0,3],[1,2],[3,4],[4,2],[2,5],[4,5]] #link
#C=[10,2,8,5,10,8,7,10] #Capacity=15 

#E=[[0,1],[1,3],[0,3],[1,2],[3,4],[3,2],[2,5],[4,5]] #link
#C=[10,2,8,8,7,6,10,10] #Capacity=17 

#E=[[0,1],[1,4],[0,3],[1,2],[3,4],[3,2],[2,5],[4,5]] #link
#C=[5,5,15,5,5,5,15,5] #Capacity=15 
#
E=[[0,1],[1,4],[0,3],[1,2],[3,4],[3,2],[2,5],[4,5]] #link
C=[6,3,6,4,4,3,5,5] #Capacity=10 

#E=[[0,1],[1,3],[0,2],[2,1],[3,2],[2,4],[4,3],[3,5],[4,5]] #link
#C=[16,12,13,4,9,14,7,20,4] #Capacity =???



def DFS_UNdirected(V,E1,T):
    color=[0]*n
    pred=[]
    curr=[] 
    u=0
    def DFS_visit(u):
        color[u]=1
        neighbor_of_u=[]
        for j in E1:
            if j[0]==u:
               neighbor_of_u.append(j[1])
        for i in neighbor_of_u:
            if color[i]==0:
                color[i]=1
                pred.append(u)
                curr.append(i)
                DFS_visit(i)
        color[u]=2
    DFS_visit(u)
    result=[]
    for i in range(len(curr)):
        result.append([pred[i],curr[i]]) 
    path=[] 
    for i in result: #turn from step to step to path from source to tank
        if i[1]!=T:
            path.append(i)
        else:
            path.append(i)
            break   
    try:
        if  path[-1][1]!=T:
            path=[]
    except: path=[]
    return path

def find_flow_in_path(V,E1,flow,C2,path):    
    flow_in_path=[]# flow capacity of each pipe in part
    for i in path:
        ID = E2.index(i)
#        flow_in_path.append(remain_capacity[ID])
        if flow[ID]!=0:
            flow_in_path.append(C2[ID]-flow[ID])
        else:
            flow_in_path.append(C2[ID])
    return flow_in_path

def find_delta(flow_in_path,E1,C1,remain_capacity):
    if min(flow_in_path)!=0:
        delta=min(flow_in_path)      
    else:
        for i in flow_in_path:
            if i<=0:
                ID1=flow_in_path.index(i)
                ID2 = E1.index(path[ID1])
                ID3 = E2.index(path[ID1])                
                if remain_capacity[ID3]!=0:
                    flow_in_path[ID1]=remain_capacity[ID3]#C2[ID3]-flow[ID3]
                    print('C1[ID2],flow[ID3]',C2[ID3],flow[ID3])
                elif remain_capacity[ID3]<=0:
                    flow_in_path[ID1]=0        
#        flow_in_path[ID1]=C2[ID2]#min(C2[ID2],remain_capacity[ID3])
        delta=min(flow_in_path)
    print('flow_in_path',flow_in_path)
    if delta<0:
        delta=0
    return delta

def flow_in_network (flow,delta,E,path):
    for i in range(int(len(flow)/2)):
        for j in path:
            if E[i]==j:
                flow[i]+=delta
                flow[i+int(len(flow)/2)]+=delta
    return flow

def remove_link(flow,E1,E2,C2,remain_capacity,delta):
    a=int(len(remain_capacity)/2)
    for i in range(a):
        try:
            if (remain_capacity[i]<=0):
                E1.remove(E2[i])
            if remain_capacity[i+a]>C2[i+a]:
                E1.remove(E2[i+a])
        except:
            continue
#            C1.remove(C2[i])
    return E1

link_number=len(E)
flow=[0]*2*link_number
#################### loop start here ##############
E1=E.copy()
E2=E.copy()
C1=C.copy()
C2=C.copy()
for i in range(link_number):
    E1.append([E[i][1],E[i][0]])
    E2.append([E[i][1],E[i][0]])
    C1.append(0)
    C2.append(C[i])   
        
    
remain_capacity=[x - y for x, y in zip(C2, flow)]
print('remain_capacity',remain_capacity)
print('*********************************************************************')


for jj in range (20):   
    print('Step:',jj+1)
    path=DFS_UNdirected(V,E1,T)
    if path==[]:
        break
    print('path', path)
    flow_in_path=find_flow_in_path(V,E1,flow,C2,path)
    print('flow_in_path', flow_in_path) 
    delta=find_delta(flow_in_path,E1,C1,remain_capacity)
      
    if delta<=0:
        break 
    print('delta', delta)
   
    flow=flow_in_network (flow,delta,E2,path)
    for i in range(link_number):
        remain_capacity[i]=C2[i]-flow[i]
        remain_capacity[i+link_number]=flow[i]

    print('remain_capacity \n',remain_capacity)
    print('flow\n',flow)
    print('C2\n',C2)
    E1=E2.copy()
    E1=remove_link(flow,E1,E2,C2,remain_capacity,delta)  
    print('E1',E1)
    
    MAX_FLOW=0
    for i in E2:
        if i[1]==T:
            id_pipes_tank=E2.index(i)
            MAX_FLOW+=flow[id_pipes_tank]
    print('MAX_FLOW =',MAX_FLOW)
    print('=========================')    
    
    

print('flow',flow)
print('MAX_FLOW =',MAX_FLOW)
 


















           