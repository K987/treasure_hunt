import layout as ly
import networkx as nx
import matplotlib.pyplot as plt

def label_dict(graph: nx.Graph):
    ret = {}
    for e in graph.edges.data():
        ret[(e[0], e[1])] = e[2]['port_in']
    return ret

def show_graph(graph, agent, neighbours):
    pos = ly.hierarchy_pos(graph, agent)
    nx.draw_networkx(graph, pos=pos, node_color=['green' if node == agent else 'red' if node.is_agent_here else 'green' for node in graph.nodes])
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=label_dict(graph))
    plt.show()
