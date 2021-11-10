# https://networkx.org/documentation/stable/tutorial.html
import networkx as nx
from networkx.classes.reportviews import EdgeDataView
import agent as a
import node as n
import draw as d
import graphs as g
from typing import List
from typing import Tuple
import sys

graph = None
start = None
end = None
neighbours = None

if (sys.argv[1] == '1'):
    graph, start, end, neighbours = g.graph_1() 
else: 
    graph, start, end, neighbours = g.graph_2() 

agent = a.Agent(graph, start, end)

# graph, agent, end = create_graph(10, [1,1])

speed = float(sys.argv[2])

draw = d.Drawer(speed)

agent.traverse(after_visit=draw.show_graph)