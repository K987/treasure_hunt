# https://networkx.org/documentation/stable/tutorial.html
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.reportviews import EdgeDataView
import agent as a
import node as n
import layout as Layout
from typing import List
from typing import Tuple

num29 = [1,1,1,1,1,1,1,0,1,1] #29
num29.reverse()

num5 = [0,0,0,0,1,1,1,0,1,1] #5
num5.reverse()

def create_graph(child_count, pebbles = []) -> Tuple[nx.Graph, a.Agent, List[n.Node]]:
    graph = nx.Graph()
    agent = a.Agent()
    graph.add_node(agent)
    nodes = []
    for i in range(0, child_count):
        pebble = '0' if len(pebbles) <= i else str(pebbles[i]) 
        node = n.Node(i, pebble)
        nodes.append(node)
        graph.add_node(node)
        graph.add_edge(agent, node, port_in=i)
    return graph, agent, nodes

graph, agent, neighbours = create_graph(10, [1,1])

neighbours[0].is_agent_here = True

def label_dict(graph: nx.Graph):
    ret = {}
    for e in graph.edges.data():
        ret[(e[0], e[1])] = e[2]['port_in']
    return ret


dict = label_dict(graph)
print(dict)

pos = Layout.hierarchy_pos(graph, agent)
nx.draw_networkx(graph, pos=pos, node_color=['green' if node == agent else 'red' if node.is_agent_here else 'green' for node in graph.nodes])
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=label_dict(graph))
plt.show()
