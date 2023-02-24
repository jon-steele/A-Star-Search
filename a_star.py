import copy
from path import Path
from functions import cost
from functions import heuristic
from functions import number_to_city

# frontier will hold all of the paths we have considered
frontier = []

def path_finder(start, goal):
    
    if start == goal:
        return 0
    
    path = Path(start)
    frontier.append(path)
    
    goal_reached = 0
    
    # Loop until the first goal has been found
    while goal_reached == 0:
        
        # Keep track of the best value path we've seen, the path index, and the next node index
        best_value = 99999
        best_path = -1 # index of path in frontier
        best_next = -1 # number value of the next city
        
        # Loop through each path in frontier
        for p in frontier:
            
            # Check each possible move
            for x in range(0, 13):
                
                # Skip if the node has been visited
                if x in p.visited_nodes:
                    continue
                
                # Calculate the heuristic and cost function for each possible move
                a_function = p.cost + cost(p.visited_nodes[-1], x) + heuristic(x, goal)  # And add the heuristic of that node, too.
                
                # We need to instantiate this path to check if we have encountered it before.
                consideration = copy.deepcopy(p)
                consideration.move(x, cost(p.visited_nodes[-1], x))
                
                # If we have a contender for the next best path, we store the parameter
                if a_function < best_value and not path_exists(consideration):
                    best_path = p
                    best_next = x
                    best_value = a_function
                    if x == goal:
                        goal_reached = 1
                    
            
        # Once we have considered all possible moves, we traverse the best one, and add the path to our frontier
        newpath = copy.deepcopy(best_path)
        newpath.move(best_next, cost(best_path.visited_nodes[-1], best_next))
        frontier.append(newpath)
        
    result = copy.deepcopy(frontier[-1])
    for x in result.visited_nodes:
        print (x)
    

def path_exists(path):
    for p in frontier:
        if p.visited_nodes == path.visited_nodes:
            return True
    return False
