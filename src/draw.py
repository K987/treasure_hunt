from agent import Agent
import layout as ly
import networkx as nx
import matplotlib.pyplot as plt

class Drawer:

    def __init__(self, wait):
        self.__wait_time = wait

    def __get_labels_dict(self, graph: nx.Graph):
        ret = {}
        for e in graph.edges.data():
            ret[(e[0], e[1])] = e[2]['port_in']
        return ret

    def __get_node_colors(self, graph: nx.Graph, agent):
        ret = []
        for n in graph.nodes:
            if (n == agent):
                ret.append('yellow')
            elif (n.is_agent_here):
                ret.append('green')
            else:
                ret.append('red')
        return ret

    def __get_agent_state(self, agent: Agent):
        ret = 'encoded: ' + agent.code + ', finished: ' + str(agent.is_code_ended())
        if (agent.is_code_ended()):
            ret = ret + ', decoded: ' + str(agent.to_port_number())
        return ret        

    def __wait(self):
        if (self.__wait_time > 0):
            plt.pause(self.__wait_time)
        else:
            plt.waitforbuttonpress()

    def show_graph(self, graph, agent):
        pos = ly.hierarchy_pos(graph, agent)
        nx.draw_networkx(graph, pos=pos, node_color=self.__get_node_colors(graph, agent))
        nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=self.__get_labels_dict(graph))
        title = self.__get_agent_state(agent)
        plt.title(title)
        plt.draw()
        self.__wait()
        plt.clf()

