class Path:
    
    # Each path has a cost, as well as an array of the visited nodes
    
    cost = 0
    visited_nodes = []
    
    # Constructor
    def __init__(self, start_node):
        self.cost = 0
        self.visited_nodes = [start_node]
        
    # move will a node onto the path, and increase it's cost
    # node is an integer value representing the city
    # cost is a number value representing the cost between this path's most recent node, and node
    def move(self, node, cost):
        self.visited_nodes.append(node)
        self.cost += cost