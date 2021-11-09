import networkx.algorithms.traversal.breadth_first_search as bfs
from  networkx import Graph as G
from typing import List

class Agent:

    def __init__(self, graph, start_node, destination_node):
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
        

    def to_port_number(self, code) -> int:
        decoded = code[1:len(code)-2:2]
        print(code, 'is stripped to', decoded, '=', int(decoded,2))
        return int(decoded,2)

    def move_to(self, new_node): 
        self.current_node.is_agent_here = False
        self.current_node = new_node
        self.current_node.is_agent_here = True

    def list_neighbours(self):
        return list(bfs.bfs_edges(self.graph, self.current_node, depth_limit=1, sort_neighbors=lambda nodes: sorted(nodes)))    
    
    def move_to_first_milestone(self, after_visit):
        code = self.read_neighbours(0, 2, after_visit)

        if code == '11': 
            print('start node is a milestone')
            return

        max = 0
        max_node = None
        
        for n in self.list_neighbours():
            deg = self.graph.degree[n[1]]
            if (deg > max):
                max = deg
                max_node = n

        print('moving to node:', max_node[1])        
        self.move_to(max_node[1])



    def traverse(self, after_visit=None):
        self.move_to_first_milestone(after_visit)
 
        skip_count = 2 if self.start_node is self.current_node else 1

        case = self.choose_case(skip_count, after_visit)

        print('Looking for a path of length:', case)

        codes = self.visit_neighbours(case, skip_count + 2, after_visit)

        print('following path:', codes)

        if self.current_node is not self.start_node:
            self.move_to(self.start_node)
                
            if callable(after_visit):
                after_visit(self.graph, self)



        for port in codes:
            if self.current_node != self.start_node:
                port += 1
            self.move_to(self.get_neighbour(port))
            if callable(after_visit):
                after_visit(self.graph, self)
        
        if callable(after_visit):
            after_visit(self.graph, self)
            after_visit(self.graph, self)

        if self.current_node != self.destination_node:
            raise RuntimeError("nem ért célba")

    def get_neighbour(self, index):
        nodes = self.list_neighbours()
        return nodes[index][1]



    def visit_neighbours(self, case, skip_count, after_visit=None) -> List[int]:
        codes = []
        code = ''

        current_node = self.current_node

        nodes = self.list_neighbours()



        for n in nodes[skip_count:]:

            self.move_to(n[1])
            code += n[1].pebble
            if callable(after_visit):
                after_visit(self.graph, self)
            self.move_to(current_node)

            if code.endswith("00") and len(code) % 2 == 0:
                # decode, add to codes
                codes.append(self.to_port_number(code))
                code = ''
            
            if case == len(codes):
                break

        
        if callable(after_visit):
            after_visit(self.graph, self)

        return codes  

    def read_neighbours(self, start, end, after_visit=None) -> str:
        code = ''
        current_node = self.current_node

        nodes = self.list_neighbours()

        for n in nodes[start:end]:

            self.move_to(n[1])
            code += n[1].pebble
            if callable(after_visit):
                after_visit(self.graph, self)
            self.move_to(current_node)
        return code

    def choose_case(self, skip_count, after_visit) -> int:
        code = self.read_neighbours(skip_count, skip_count+2, after_visit)
        if code == '11': return 3
        else: return 4


        

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def __append_code(self, pebble):
        self.code = pebble + self.code
