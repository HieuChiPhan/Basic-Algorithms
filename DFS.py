#Test input
n=6
V=list(range(n)) #node
E=[[0,1],[1,3],[0,3],[1,4],[3,4],[4,2],[2,5],[4,5],[1,2]] #link-edges

#n=16
#V=list(range(n)) #node
#E=[[0,1],[1,2],[2,10],[2,11],[1,3],[3,12],[3,4],[4,13],[0,6],[0,8],[4,5],[5,6],[15,9],[5,9],[6,7],[9,7],[8,7],[8,14]] #link-edges
#print(len(E))

def DFS_directed(V,E):
    n=len(V)
    color=[0]*n
    pred=[]
    curr=[] 
    u=0
    def DFS_visit(u):
        color[u]=1
        neighbor_of_u=[]
        for j in E:
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
    return result

def DFS_UNdirected(V,E):
    color=[0]*n
    pred=[]
    curr=[] 
    u=0
    def DFS_visit(u):
        color[u]=1
        neighbor_of_u=[]
        for j in E:
            if j[0]==u:
               neighbor_of_u.append(j[1])
            if j[1]==u:
               neighbor_of_u.append(j[0])
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
    return result
    
result=DFS_directed(V,E)   
print (result) 






