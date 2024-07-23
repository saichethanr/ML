from collections import deque

def bfs(graph,start,goal,heuristic):
    queue = deque([(start,heuristic[start])])
    visited = set()
    #dictionary to keep track of parent of each node
    parent = {start:None}
    #to keep the track of the cost needed to reach each node 
    cost = {start: 0}
    while queue:
        queue = deque(sorted(list(queue),key=lambda x:x[1]))
        current_node, current_heuristic = queue.popleft()
        if current_node is visited:
            continue
        visited.add(current_node)
        if current_node==goal:
            break
        
        for neighbour,edge_cost in graph[current_node]:
            if neighbour is not visited:
                queue.append((neighbour,heuristic[neighbour]))
                parent[neighbour] = current_node
                cost[neighbour] = cost[current_node] + edge_cost
    path =[]
    node = goal
    total_cost = cost.get(goal,0)
    while node is not None:
            path.append(node)
            node =parent[node]
    path.reverse()
    
    return path,total_cost
        
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3), ('E', 4)],
    'C': [('F', 5), ('G', 6)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 0,
    'E': 2,
    'F': 3,
    'G': 1
}

start = 'A'
goal = 'D'

path, total_cost = bfs(graph, start, goal, heuristic)
print("Best First Search Path:", path)
print("Total Cost:", total_cost)