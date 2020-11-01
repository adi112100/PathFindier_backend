import sys
sys.setrecursionlimit(10**6) 

def dfs_creategraph(row, col, walls):
    adjlst = [[] for i in range(row*col)]
    node = 0 #unique node
    for i in range(row):
        for j in range(col):
            
            if node not in walls:
                if i==0 and j==0:
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node+col not in walls: adjlst[node].append(node+col)
                elif i==row-1 and j==col-1:
                    if node-col not in walls: adjlst[node].append(node-col)
                    if node-1 not in walls: adjlst[node].append(node-1)
                elif i==0 and j==col-1:
                    if node+col not in walls: adjlst[node].append(node+col)
                    if node-1 not in walls: adjlst[node].append(node-1)
                elif i==row-1 and j==0:
                    if node-col not in walls: adjlst[node].append(node-col)
                    if node+1 not in walls: adjlst[node].append(node+1)
                elif i==0:
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node+col not in walls: adjlst[node].append(node+col)
                    if node-1 not in walls: adjlst[node].append(node-1)
                elif i==row-1:
                    if node-col not in walls: adjlst[node].append(node-col)
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node-1 not in walls: adjlst[node].append(node-1)
                elif j==0:
                    if node-col not in walls: adjlst[node].append(node-col)
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node+col not in walls: adjlst[node].append(node+col)
                elif j==col-1:
                    if node-col not in walls: adjlst[node].append(node-col)
                    if node+col not in walls: adjlst[node].append(node+col)
                    if node-1 not in walls: adjlst[node].append(node-1)
                else:
                    if node-col not in walls: adjlst[node].append(node-col)
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node+col not in walls: adjlst[node].append(node+col)
                    if node-1 not in walls: adjlst[node].append(node-1)
            node+=1
    return adjlst

# final_path=[]
# streamnodes=[]

# def dfs(adj_lst, current_node, end, path):
#     global final_path, streamnodes

#     if current_node in streamnodes:
#         return 0
#     if current_node == end:
#         path.append(current_node)
#         streamnodes.append(current_node)

#         final_path = path.copy()
#         return 0
#     else:
#         path.append(current_node)
#         streamnodes.append(current_node)

#         for node in adj_lst[current_node]:
#             dfs(adj_lst, node, end, path)
    
#     return 0

    
    


# def dfs_algorithm(row,col,start,end,walls):
    
#     adj_list = dfs_creategraph(row,col,walls)
#     path = []
#     dfs(adj_list, start, end, path)

#     return(streamnodes, final_path)

def dfs_algorithm(row,col,start,end,walls):
    final_path=[]
    streamnodes=[]
    adj_list = dfs_creategraph(row,col,walls)
    for index,item in enumerate(adj_list): print(index,item)
    stk = [start]
    node = start
    while(len(stk)!=0):
        streamnodes.append(node)
        final_path.append(node)
        
        if len(final_path)>=2:
            while final_path[-2] not in adj_list[final_path[-1]]:
                final_path.pop(-2)

        for nodes in adj_list[node]:
            if nodes not in streamnodes: stk.append(nodes)
        
        node = stk.pop(-1)
        if node==end:
            streamnodes.append(node)
            final_path.append(node)
            return (streamnodes, final_path)


# print(dfs_algorithm(5,5,0,24,[6,7,8,11,12,13,17,18,23]))