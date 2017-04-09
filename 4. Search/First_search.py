# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    
    openPositions = []
    current_pos = [0, init[0], init[1]]
    
    while(True):
        
        # Check for success
        if current_pos[1] == goal[0] and current_pos[2] == goal[1]:
            path = current_pos
            break;

        # Loop over possible movements
        for movement in delta:
            # Next position is current position + possible movement
            next_pos = [current_pos[0]+cost, movement[0]+current_pos[1], movement[1]+current_pos[2]]
            # Make sure next position is in the grid and not a wall
            if next_pos[1] > -1 and next_pos[2] > -1 and next_pos[1] < len(grid) and next_pos[2] < len(grid[next_pos[1]]) and grid[next_pos[1]][next_pos[2]] == 0:
                # Add that next_pos to open positions list
                openPositions.append(next_pos)
                # Mark that grid place as -1 so it isn't added again to open positions
                grid[next_pos[1]][next_pos[2]] = -1
        
        # Fail if no open positions left
        if len(openPositions) == 0:
            path = "fail"
            break
        
        # Sort open positions based on their cost (or g_value), lowest first
        openPositions.sort(key=lambda x: x[0])
        
        # Set current position to the open position with the lowest cost, and remove that position from open positions
        current_pos = openPositions.pop()
        
        
    return path
    
print search(grid, init, goal, cost)
