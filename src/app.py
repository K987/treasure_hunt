# https://networkx.org/documentation/stable/tutorial.html
import networkx as nx
import matplotlib.pyplot as plt
import agent as a
import node as n
import layout as Layout
from typing import List
from typing import Tuple

num29 = [1,1,1,1,1,1,1,0,1,1] #29
num29.reverse()

num5 = [0,0,0,0,1,1,1,0,1,1] #5
num5.reverse()

def create_graph(child_count, pebbles = []) -> Tuple[nx.Graph, List[n.Node]]:
    graph = nx.Graph()
    agent = a.Agent()
    graph.add_node(agent)
    nodes = []
    for i in range(0, child_count):
        print(str(i) + " " + str(len(pebbles)))
        pebble = '0' if len(pebbles) <= i else str(pebbles[i]) 
        node = n.Node(i, pebble)
        nodes.append(node)
        graph.add_node(node)
        graph.add_edge(agent, node, port_in=i)
    return graph, agent, nodes

graph, agent, neighbours = create_graph(10, [1,1])

neighbours[0].is_agent_here = True


pos = Layout.hierarchy_pos(graph, agent)
nx.draw_networkx(graph, pos=pos, node_color=['green'] + ['red' if node.is_agent_here else 'green' for node in neighbours])
plt.show()
