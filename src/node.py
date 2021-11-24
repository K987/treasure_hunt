class Node:
    id = 0
    def __init__(self, port_in: int, pebble='0', is_agent_here=False, is_path_node=False):
        self.port_in = port_in
        self.pebble = pebble
        self.is_agent_here = is_agent_here
        self.id = Node.id
        self.is_path_node = is_path_node
        Node.id += 1
    
    def __str__(self):
        return str(self.pebble)
    
    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.id < other.id