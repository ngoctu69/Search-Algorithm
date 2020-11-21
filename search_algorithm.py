import pygame
import graphUI
from node_color import white, yellow, black, red, blue, purple, orange, green
import math

"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""
def printPath(graph, edges, edge_id, start, goal, Parent):
    node=goal
    graph[start][3]=orange
    graph[goal][3]=purple
    graphUI.updateUI()
    while node !=start:
        edges[edge_id(node, Parent[node])][1] = green
        graphUI.updateUI()
        node=Parent[node]
    return


def BFS(graph, edges, edge_id, start, goal):
    queue = [start]
    Visited = [False]*len(graph)
    Parent = [-1]*len(graph)

    Visited[start] = True #dinh bat dau
    graph[start][3]=red
    graphUI.updateUI()
    pygame.time.delay(300) 

    while len(queue)!=0:
        cur=queue.pop(0)

        graph[cur][3]=yellow
        graphUI.updateUI()
        pygame.time.delay(300) 

        if cur==goal:
            printPath(graph, edges, edge_id, start, goal, Parent)
            return

        if Parent[cur]!=-1: #Neu co dinh cha truoc thi to mau xanh duong cho dinh cha
            graph[Parent[cur]][3]=blue
            graphUI.updateUI()
            pygame.time.delay(300) 

        node = graph[cur]
        for adjacency_node in node[1]:
            if adjacency_node==goal:
                Parent[adjacency_node]=cur
                printPath(graph, edges, edge_id, start, goal, Parent)
                return

            if Visited[adjacency_node]==False:
                queue.append(adjacency_node)
                Visited[adjacency_node]=True
                Parent[adjacency_node]=cur

                #Cho canh mau trang
                edges[edge_id(cur, adjacency_node)][1] = white
                graphUI.updateUI()
                pygame.time.delay(300) 

                #Cho node vua tim duoc mau do
                graph[adjacency_node][3]=red
                graphUI.updateUI()
                pygame.time.delay(300) 
        
        graph[cur][3]=blue #cho dinh da xet mau blue
        graphUI.updateUI()
        pygame.time.delay(300) 
    

def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    # TODO: your code
    stack = [start]
    Visited = [False]*len(graph)
    Parent = [-1]*len(graph)

    Visited[start] = True #dinh bat dau
    graph[start][3]=red
    graphUI.updateUI()
    pygame.time.delay(300) 

    while len(stack)!=0:
        cur=stack.pop(0)

        graph[cur][3]=yellow
        graphUI.updateUI()
        pygame.time.delay(300) 

        if cur==goal:
            printPath(graph, edges, edge_id, start, goal, Parent)
            return

        if Parent[cur]!=-1: #Neu co dinh cha truoc thi to mau xanh duong cho dinh cha
            graph[Parent[cur]][3]=blue
            graphUI.updateUI()
            pygame.time.delay(300) 

        node = graph[cur]
        for adjacency_node in node[1]:
            if adjacency_node==goal:
                Parent[adjacency_node]=cur
                printPath(graph, edges, edge_id, start, goal, Parent)
                return

            if Visited[adjacency_node]==False:
                stack.append(adjacency_node)
                Visited[adjacency_node]=True
                Parent[adjacency_node]=cur

                #Cho canh mau trang
                edges[edge_id(cur, adjacency_node)][1] = white
                graphUI.updateUI()
                pygame.time.delay(300) 

                #Cho node vua tim duoc mau do
                graph[adjacency_node][3]=red
                graphUI.updateUI()
                pygame.time.delay(300) 
                break
            
        if len(stack)==0:
            stack.append(Parent[cur])
        
        graph[cur][3]=blue #cho dinh da xet mau blue
        graphUI.updateUI()
        pygame.time.delay(300)

def getCost(a, b):
    x=a[0]
    y=b[0]
    sq1=(x[0]-y[0])*(x[0]-y[0])
    sq2=(x[1]-y[1])*(x[1]-y[1])
    return math.sqrt(sq1 + sq2)

def UCS(graph, edges, edge_id, start, goal):
    Open=[start]
    Close=[]
    Parent=[-1]*len(graph)
    Cost=[999999]*len(graph)
    Cost[start]=0

    graph[start][3]=red
    graphUI.updateUI()
    pygame.time.delay(300)

    while (len(Open)!=0):
        Min=Cost[Open[0]]
        cur=Open[0]
        for i in Open:
            if Cost[i] < Min:
                Min=Cost[i]
                cur=i

        graph[cur][3]=yellow
        graphUI.updateUI()
        pygame.time.delay(300)
        
        curNode=graph[cur]

        for adjacency_node in curNode[1]:
            if Close.count(adjacency_node) == 0: #Kiem tra node co trong Close chua
                if Open.count(adjacency_node)!=0: #Neu node da co trong Open thi kiem tra lai chi phi, neu nho hon thi cap nhat
                    newCost = Cost[cur] + getCost(graph[cur], graph[adjacency_node])
                    if Cost[adjacency_node] > newCost:
                        Cost[adjacency_node] = newCost
                        Parent[adjacency_node]=cur
                else:
                    Open.append(adjacency_node)
                    Parent[adjacency_node]=cur

                #Cho canh mau trang
                edges[edge_id(cur, adjacency_node)][1] = white
                graphUI.updateUI()
                pygame.time.delay(300) 

                #Cho node vua tim duoc mau do
                graph[adjacency_node][3]=red
                graphUI.updateUI()
                pygame.time.delay(300)

        Close.append(cur)
        Open.remove(cur)

        if Close.count(goal)!=0:
            printPath(graph, edges, edge_id, start, goal, Parent)
            return
        
        graph[cur][3]=blue #cho dinh da xet mau blue
        graphUI.updateUI()
        pygame.time.delay(300)

        for i in Open:
            if Parent[i]==cur:
                newCost = Cost[cur] + getCost(graph[cur], graph[i])
                if Cost[i] > newCost:
                    Cost[i] = newCost
    
    print("Implement Uniform Cost Search algorithm.")
    pass

def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code
    Open=[start]
    Close=[]
    Parent=[-1]*len(graph)
    Cost=[999999]*len(graph)
    Cost[start]=0
    f=[999999]*len(graph) #f= cost + cost(cur,goal)
    f[start]= getCost(graph[start], graph[goal])


    graph[start][3]=red
    graphUI.updateUI()
    pygame.time.delay(300)

    while (len(Open)!=len(graph)):
        for i in range(len(graph)):
            f[i]=Cost[i]+ getCost(graph[i], graph[goal])

        Min=f[Open[0]]
        cur=Open[0]
        for i in Open:
            if f[i] < Min:
                Min=f[i]
                cur=i

        graph[cur][3]=yellow
        graphUI.updateUI()
        pygame.time.delay(300)
        
        curNode=graph[cur]

        for adjacency_node in curNode[1]:
            if Close.count(adjacency_node) == 0: #Kiem tra node co trong Close chua
                if Open.count(adjacency_node)!=0: #Neu node da co trong Open thi kiem tra lai cost, neu nho hon thi cap nhat
                    newCost = Cost[cur] + getCost(curNode, graph[adjacency_node])
                    if Cost[adjacency_node] > newCost:
                        Cost[adjacency_node] = newCost
                        Parent[adjacency_node]=cur
                else:
                    Open.append(adjacency_node)
                    Parent[adjacency_node]=cur

                #Cho canh mau trang
                edges[edge_id(cur, adjacency_node)][1] = white
                graphUI.updateUI()
                pygame.time.delay(300) 

                #Cho node vua tim duoc mau do
                graph[adjacency_node][3]=red
                graphUI.updateUI()
                pygame.time.delay(300)

        Close.append(cur)
        Open.remove(cur)

        if Close.count(goal)!=0:
            printPath(graph, edges, edge_id, start, goal, Parent)
            return
        
        graph[cur][3]=blue #cho dinh da xet mau blue
        graphUI.updateUI()
        pygame.time.delay(300)

        for i in Open:
            if Parent[i]==cur:
                newCost = Cost[cur] + getCost(curNode, graph[i])
                if Cost[i]> newCost:
                    Cost[i] = newCost

    print("Implement A* algorithm.")
    pass


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                        [0] : (x,y) coordinate in UI
                        [1] : adjacent node indexes
                        [2] : node edge color
                        [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()
