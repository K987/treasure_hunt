class Node:
    def __init__(self, port_in: int, pebble='0'):
        self.portIn = port_in
        self.pebble = pebble
    
    def __str__(self):
        ret = str(self.portIn) + '\n' + self.pebble
        return ret
    
    def __repr__(self):
        return str(self.portIn)

    def __lt__(self, other):
        return self.portIn < other.portIn