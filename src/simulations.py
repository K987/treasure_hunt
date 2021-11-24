import networkx as nx
from networkx.classes.reportviews import EdgeDataView
import numpy as np
import agent as a
import agent_dfs as adfs
import node as n
import draw as d
import graphs as g
from typing import List
from typing import Tuple
import sys



def simulate(): 
    steps = []
    steps_dfs = []
    diameter = []
    size=[]
    milestone_distance = []
    milestone_count = []
    path_distance = []

    for j in range(20):
        for i in range(2*j):
            n.Node.id = 0

            print("simulation step %i, %i"%(i, j))
            path_count = j + 1
            populate_count = i

            graph, start, end, neighbours = g.generate(start=[g.start_1, g.start_2], path=[g.path_1, g.path_2, g.path_3], count=path_count)
            
            diam = nx.diameter(graph)
            milestone_distance.append(diam / path_count)
            path_distance.append(diam )

            g.populate(graph, neighbours, populate_count)

            diameter.append(nx.diameter(graph))
            size.append(graph.size())
            milestone_count.append(path_count)

            agent1 = a.Agent(graph, start, end)
            agent2 = adfs.AgentDfs(graph, start, end)

            agent1.traverse()
            agent2.traverse()

            steps.append(agent1.step_count)
            steps_dfs.append(agent2.step_count)
    
    np.save("simulation.npy", (size, diameter, path_distance, milestone_distance, milestone_count, milestone_count, steps, steps_dfs))
    return size, diameter, path_distance, milestone_distance, milestone_count, milestone_count, steps, steps_dfs

def load():
    return np.load("simulation.npy")
