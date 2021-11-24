import networkx.algorithms.traversal.breadth_first_search as bfs
from  networkx import Graph as G
from typing import List

from networkx.classes.function import neighbors

class AgentDfs:

    def __init__(self, graph, start_node, destination_node):
        self.step_count = 0
        self.name = 'agent'
        self.code = ''
        # the entry point of the graph
        self.start_node = start_node
        # where the agent actually stands
        self.current_node = start_node
        # the target node to find the way
        self.destination_node = destination_node
        # The graph 
        self.graph = graph

    def move_to(self, new_node): 
        self.current_node.is_agent_here = False
        self.current_node = new_node
        self.current_node.is_agent_here = True
        self.step_count += 1

    def list_neighbours(self):
        return list(bfs.bfs_edges(self.graph, self.current_node, depth_limit=1, sort_neighbors=lambda nodes: sorted(nodes)))    
    
    

    def traverse(self, after_visit=None):
        visited_nodes = []

        while(self.current_node != self.destination_node):
            visited_nodes.append(self.current_node)

            neighbours = self.list_neighbours()
            unvisited_neighbours = [node for node in neighbours if node[1] not in visited_nodes]

            if len(unvisited_neighbours) == 0:
                self.move_to(neighbours[0][1])
            else: 
                self.move_to(unvisited_neighbours[0][1])
            
            if callable(after_visit):
                after_visit(self.graph, self)
        pass

    def get_neighbour(self, index):
        nodes = self.list_neighbours()
        if(len(nodes) <= index): return None
        return nodes[index][1]

    def get_step_count(self):
        return self.step_count

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
