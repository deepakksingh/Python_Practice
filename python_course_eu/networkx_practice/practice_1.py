import networkx as nx
from matplotlib import pyplot as plt

G = nx.Graph()

print(G.nodes())
print(G.edges())

print(type(G.nodes()))
print(type(G.edges()))

G.add_node("a")
G.add_nodes_from(["b","c"])

print("Nodes of graph:")
print(G.nodes())
print("Edges of graph:")
print(G.edges())

G.add_edge(1,2)
print(G.edges())
edge = ("d","e")
G.add_edge(*edge)
G.add_edge("c","d")

print(G.nodes())
print(G.edges())

nx.draw(G)
plt.savefig("random1.png")
plt.show()