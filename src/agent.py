import networkx.algorithms.traversal.breadth_first_search as bfs

class Agent:

    def __init__(self):
        self.name = 'agent'
        self.code = ''

    def is_code_ended(self) -> bool:
        return len(self.code) > 2 and self.code.startswith('00')

    def to_port_number(self) -> int:
        start = 3 if self.is_code_ended() else 1
        decoded = self.code[start::2]
        print(self.code, 'is stripped to', decoded)
        return int(decoded,2)

    def visit_neighbours(self, g, after_visit=None):
        for n in bfs.bfs_edges(g, self, depth_limit=1, sort_neighbors=lambda nodes: sorted(nodes)):
            
            n[1].is_agent_here = True
            self.__append_code(n[1].pebble)

            if callable(after_visit):
                after_visit(g, self)

            n[1].is_agent_here = False

            if (self.is_code_ended()):
                break

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def __append_code(self, pebble):
        self.code = pebble + self.code
