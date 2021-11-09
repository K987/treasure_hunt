# https://networkx.org/documentation/stable/tutorial.html
import networkx as nx
from networkx.classes.reportviews import EdgeDataView
import agent as a
import node as n
import draw as d
import graphs as g
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

graph, start, end, neighbours = g.graph_2() 
agent = a.Agent(graph, start, end)

# graph, agent, end = create_graph(10, [1,1])

draw = d.Drawer(0.25)

agent.traverse(after_visit=draw.show_graph)