def minimax(depth,nodeIndex,maximizingPlayer,values,alpha,beta,path):
    #When the depth is 3, the function reaches a terminal node. It returns the value of this node and the path taken to reach it.
    if depth==3:
        return values[nodeIndex],path+[nodeIndex]
    if maximizingPlayer:
        best = float('-inf')
        best_path =[]
        for i in range(2):
            val,new_path = minimax(depth+1,nodeIndex*2+i,False,values,alpha,beta,path+[nodeIndex])
            if val>best:
                best = val
                best_path= new_path
        return best,best_path
    else:
        best = float('inf')
        best_path = []
        for i in range(2):
            val,new_path = minimax(depth+1,nodeIndex *2 +1, True, values,alpha,beta,path+[nodeIndex])
            if val<best:
                best = val
                best_path = new_path
        return best,best_path
        
values = [3, 5, 2, 9, 12, 5, 23, 23]
# Start the Min-Max algorithm
optimal_value, optimal_path = minimax(0, 0, True, values, float('-inf'), float('inf'), [])
print("The optimal value is:", optimal_value)
print("The path taken is:", optimal_path)