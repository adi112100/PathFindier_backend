import math

def astar_initilaize_path(row,col):
    return [[] for i in range(row*col)]

def astar_hueristic(row,col,end):
    lst = []
    endx, endy = [end//col, end%col]
    for i in range(row*col):
        x,y = [i//col, i%col]
        lst.append(abs(endx-x) + abs(endy-y))
    
    return lst

def astar_creategraph(row, col, walls):
    adjlst = [[] for i in range(row*col)]
    node = 0 #unique node
    for i in range(row):
        for j in range(col):
            
            if node not in walls:
                if i==0 and j==0:
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node+col not in walls: adjlst[node].append(node+col)
                elif i==row-1 and j==col-1:
                    if node-1 not in walls: adjlst[node].append(node-1)
                    if node-col not in walls: adjlst[node].append(node-col)
                elif i==0 and j==col-1:
                    if node-1 not in walls: adjlst[node].append(node-1)
                    if node+col not in walls: adjlst[node].append(node+col)
                elif i==row-1 and j==0:
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node-col not in walls: adjlst[node].append(node-col)
                elif i==0:
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node+col not in walls: adjlst[node].append(node+col)
                    if node-1 not in walls: adjlst[node].append(node-1)
                elif i==row-1:
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node-col not in walls: adjlst[node].append(node-col)
                    if node-1 not in walls: adjlst[node].append(node-1)
                elif j==0:
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node+col not in walls: adjlst[node].append(node+col)
                    if node-col not in walls: adjlst[node].append(node-col)
                elif j==col-1:
                    if node-1 not in walls: adjlst[node].append(node-1)
                    if node+col not in walls: adjlst[node].append(node+col)
                    if node-col not in walls: adjlst[node].append(node-col)
                else:
                    if node+1 not in walls: adjlst[node].append(node+1)
                    if node-1 not in walls: adjlst[node].append(node-1)
                    if node+col not in walls: adjlst[node].append(node+col)
                    if node-col not in walls: adjlst[node].append(node-col)
            node+=1
    return adjlst

def astar_algorithm(row, col, start, end, walls):
    visited_path = [0 for i in range(row*col)]
    shortest_path = astar_initilaize_path(row, col)
    shortest_path_val = [math.inf for i in range(row*col)]
    hueristic_path_value = astar_hueristic(row,col,end)
    adjlst = astar_creategraph(row, col, walls)

    totalnodes = row*col
    
    streamnodes = [] #the nodes which are visited in djsktras algorithm 
    for i in range(totalnodes):
        
        if i==0:
            streamnodes.append(start)
            visited_path[start] = 1
            shortest_path[start].append(start)
            shortest_path_val[start] = 0
            for node in adjlst[start]:
                if node not in streamnodes: streamnodes.append(node)

                if  shortest_path_val[node] > shortest_path_val[start] + 1:
                    shortest_path_val[node] = shortest_path_val[start] + 1
                    shortest_path[node] = shortest_path[start].copy() 
                    shortest_path[node].append(node)
                
        else:
            
            if shortest_path_val[end]!=math.inf:
                print('isbreak')
                return ([streamnodes, shortest_path_val, shortest_path])
            else:
                minnval = math.inf
                minindex = -1
                for j in range(totalnodes):
                    if visited_path[j]==0 and shortest_path_val[j] + hueristic_path_value[j] < minnval:
                        minnval = shortest_path_val[j] + hueristic_path_value[j]
                        minindex = j
                    elif visited_path[j]==0 and shortest_path_val[j] + hueristic_path_value[j] == minnval and hueristic_path_value[j] < hueristic_path_value[minindex]:
                        minnval = shortest_path_val[j] + hueristic_path_value[j]
                        minindex = j
                
                visited_path[minindex] = 1
                
                for node in adjlst[minindex]:
                    if node not in streamnodes: streamnodes.append(node)

                    if  shortest_path_val[node] > shortest_path_val[minindex] + 1:
                        shortest_path_val[node] = shortest_path_val[minindex] + 1
                        shortest_path[node] = shortest_path[minindex].copy()
                        shortest_path[node].append(node)

    return ([streamnodes, shortest_path_val, shortest_path])






    


                
            





