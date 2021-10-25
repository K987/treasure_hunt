# https://networkx.org/documentation/stable/tutorial.html
import networkx as nx
import matplotlib.pyplot as plt
import agent as Agent
import node as Node

graph = nx.Graph()
agent = Agent.Agent()
graph.add_node(agent)

num29 = [1,1,1,1,1,1,1,0,1,1] #29
num29.reverse()

num5 = [0,0,0,0,1,1,1,0,1,1] #5
num5.reverse()

for i in range(10,0,-1):
    node = Node.Node(i, str(num5[i-1]))
    graph.add_node(node)
    graph.add_edge(agent, node)

agent.visit_neighbours(graph)
print(agent.code)
print(agent.to_port_number())

