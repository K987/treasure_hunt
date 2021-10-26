class Node:
    def __init__(self, port_in: int, pebble='0', is_agent_here=False):
        self.port_in = port_in
        self.pebble = pebble
        self.is_agent_here = is_agent_here
    
    def __str__(self):
        return self.pebble
    
    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.port_in < other.port_in

    def __hash__(self):
        return self.port_in