import networkx as nx
import queue

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        #Check if graph is empty
        if len(self.graph.nodes) == 0:
            print('Graph is empty') 
            return None

        #check to see if starting node is in graph
        if start in self.graph:

            #BFT
            if end == None:
                #list to store path traveled
                path = []

                #BFS Algorithm (from slides)
                q = queue.Queue()
                visited = []
                q.put(start)
                visited.append(start)
                while q.qsize() > 0:
                    current_node = q.get()

                    #see how you walked
                    path.append(current_node)

                    neighbors = list(self.graph.adj[current_node].keys())
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            visited.append(neighbor)
                            q.put(neighbor)
            
                #check if all nodes were traversed
                if len(path) == len(self.graph.nodes):
                    return path
                
                #Return None if not
                else:
                    print('Graph is not connected')
                    return None
            
            else:

                #BFS
                if end in self.graph:
                    #list to store path traveled
                    path = []

                    #BFS Algorithm (from slides)
                    q = queue.Queue()
                    visited = []
                    q.put(start)
                    visited.append(start)
                    while q.qsize() > 0:
                        current_node = q.get()

                        #see how you walked
                        path.append(current_node)
                        
                        #return path once end is found
                        if current_node == end:
                            return path

                        neighbors = list(self.graph.adj[current_node].keys())
                        for neighbor in neighbors:
                            if neighbor not in visited:
                                visited.append(neighbor)
                                q.put(neighbor)

                    #If while loop is finished then no path was found
                    print('No path from starting node to ending node')
                    return None
                
                else:
                    print('Ending node not in graph')
                    return None

        else:
            print('Starting node not in graph')
            return None





