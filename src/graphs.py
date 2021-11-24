# https://networkx.org/documentation/stable/tutorial.html
import networkx as nx
from networkx.classes.reportviews import EdgeDataView
import agent as a
import node as n
import draw as d
from typing import List
from typing import Tuple
import random

def encode_data(data):
  nd = ""
  for d in data:
    nd += ("10" if d == "0" else "11")
  
  return nd; 

def encode_int(number):
  return str(bin(number)[2:]).rjust(4, '0')


def add_children(graph, parent, pebbles, child_count = None):
  if child_count is None:
    child_count = len(pebbles)

  nodes = []

  for i in range(0, child_count):
        pebble = '0' if len(pebbles) <= i else str(pebbles[i]) 
        node = n.Node(i, pebble)
        nodes.append(node)
        graph.add_node(node)
        graph.add_edge(parent, node, port_in=i)
  return nodes

def start_1():
  graph = nx.Graph()
  start = n.Node(0, '0')

  L1 = add_children(graph, start, 
    "11" # first node is a milestone
    + "11" # next milestone is in 3 step distance
    + encode_data(encode_int(10)) + "00" # first step through port 10
    + encode_data(encode_int(3)) + "00" # second step through port 3
    + encode_data(encode_int(7)) + "00" # thirs step through port 7
  )

  L2 = add_children( graph, L1[10], '', 5)
  L3 = add_children( graph, L2[3], '', 8)

  end= L3[7]
  nodes = L1+L2+L3

  return graph, start, end, nodes

def start_2():
  graph = nx.Graph()
  start = n.Node(0, '0')

  L1 = add_children(graph, start, '10', 7) # first milestone is 1 step away from start node (node with max degree)
  
  milestone = L1[3]
  m1 = add_children(graph, milestone, 
    "10" # next milestone is in 4 step distance
    + encode_data(encode_int(5)) + "00" # first step from s through port 10
    + encode_data(encode_int(3)) + "00" # second step from s through port 3
    + encode_data(encode_int(7)) + "00" # thirs step from s through port 7
    + encode_data(encode_int(2)) + "00" # thirs step from s through port 7
  )

  L2 = add_children( graph, L1[5], '', 5)
  L3 = add_children( graph, L2[3], '', 8)
  L4 = add_children( graph, L3[7], '', 4)

  end= L4[2]


  nodes = L1+L2+L3+L4+m1

  return graph, start, end, nodes

# 3 long hard coded path element
def path_1(graph, start):
  L1 = add_children(graph, start, 
    "11" # next milestone is in 3 step distance
    + encode_data(encode_int(10)) + "00" # first step through port 10
    + encode_data(encode_int(3)) + "00" # second step through port 3
    + encode_data(encode_int(7)) + "00" # thirs step through port 7
  )

  L2 = add_children( graph, L1[10], '', 5)
  L3 = add_children( graph, L2[3], '', 8)

  end= L3[7]
  nodes = L1+L2+L3

  return end, nodes

# 4 long hard coded path element
def path_2(graph, start):
  L1 = add_children(graph, start, 
    "10" # next milestone is in 3 step distance
    + encode_data(encode_int(5)) + "00" # first step from s through port 10
    + encode_data(encode_int(3)) + "00" # second step from s through port 3
    + encode_data(encode_int(7)) + "00" # thirs step from s through port 7
    + encode_data(encode_int(2)) + "00" # thirs step from s through port 7
  )

  L2 = add_children( graph, L1[5], '', 5)
  L3 = add_children( graph, L2[3], '', 8)
  L4 = add_children( graph, L3[7], '', 4)

  end= L4[2]
  nodes = L1+L2+L3+L4

  return end, nodes

  # 5 long hard coded path element
def path_3(graph, start):
  L1 = add_children(graph, start, 
    "01" # next milestone is in 3 step distance
    + encode_data(encode_int(2)) + "00" # first step from s through port 10
    + encode_data(encode_int(3)) + "00" # second step from s through port 3
    + encode_data(encode_int(9)) + "00" # thirs step from s through port 7
    + encode_data(encode_int(2)) + "00" # thirs step from s through port 2
    + encode_data(encode_int(1)) + "00" # thirs step from s through port 1
  )

  L2 = add_children( graph, L1[2], '', 5)
  L3 = add_children( graph, L2[3], '', 11)
  L4 = add_children( graph, L3[9], '', 4)
  L5 = add_children( graph, L4[2], '', 8)

  end= L5[1]
  nodes = L1+L2+L3+L4+L5

  return end, nodes
  

def generate(start, path, count):
  graph, graph_start, end, nodes = start[random.randrange(0, len(start))]()

  for i in range(count-1):
    new_end, new_nodes = path[random.randrange(0, len(path))](graph, end)
    end = new_end
    nodes += new_nodes

  return graph, graph_start, end, nodes

