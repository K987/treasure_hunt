# https://networkx.org/documentation/stable/tutorial.html
import networkx as nx
from networkx.classes.reportviews import EdgeDataView
import agent as a
import agent_dfs as adfs
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

if (len(sys.argv) == 1 or sys.argv[1] == '1'):
    graph, start, end, neighbours = g.generate(start=[g.start_1], path=[g.path_3], count=1)
else: 
    graph, start, end, neighbours = g.start_2() 

agent = a.Agent(graph, start, end)
agent = adfs.AgentDfs(graph, start, end)

# graph, agent, end = create_graph(10, [1,1])

speed = 1 if len(sys.argv) < 3 else float(sys.argv[2])

draw = d.Drawer(speed)

agent.traverse(after_visit=draw.show_graph)
#agent.traverse()