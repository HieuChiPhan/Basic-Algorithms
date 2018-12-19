import numpy as np
n=6
V=list(range(n)) #node
E=[[0,1],[1,3],[0,3],[1,4],[3,4],[4,2],[2,5],[4,5],[1,2]]
neighbors=[]
for i in V:
    neighbor=[]
    for j in E:
        if i == j[0]:
            neighbor.append(j[1])
    neighbors.append(neighbor)
print(neighbors)


paths=[]
s=0
v=s
path=[]
E1=E.copy()
for j in E1:
    print(j)
    if v==j[0]:
        path.append(v)
        v=j[1]
#        E1.remove(j)
paths.append(path)
print(paths)            