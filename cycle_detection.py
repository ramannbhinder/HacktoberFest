from collections import deque,defaultdict

#Adjacency matrix
def create_adj_mat(edges):
    no_of_nodes=1+ max([e[0] for e in edges] + [e[1] for e in edges])
    adj=[[0]*no_of_nodes for i in range(no_of_nodes)]
    for e in edges:
        adj[e[0]][e[1]]=1   #directed graph
        adj[e[1]][e[0]]=1
    return adj

adj_mat=create_adj_mat([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])

#Adjacency list
def create_adj_list(edges):
    adj=defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    return adj

adj_list=create_adj_list([[0,1],[1,2],[1,3],[2,4],[3,4],[5,7],[7,6]])

def cyclebfs(adj):
    vis=set()
    # n=len(adj)
    n=max(adj)+1
    for i in range(n):
        if i in vis:
            continue
        vis.add(i)
        
        q=deque([[i,-1]])
        while q:
            node,parent=q.pop()
            for adjnode in range(n):
                # if adj[node][adjnode]:
                if adjnode in adj[node]:
                    if adjnode not in vis:
                        vis.add(adjnode)
                        # q.append([adjnode,node])      #DFS
                        q.appendleft([adjnode,node])  #BFS
                    elif adjnode!=parent:
                        print(f"cycle found at {node} - {adjnode}")
                        return
    print("No Cycle found")

# cyclebfs(adj_mat)
cyclebfs(adj_list)
