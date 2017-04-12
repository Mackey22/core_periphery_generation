import networkx as nx
import matplotlib.pyplot as plt
import math

# k=2 / math.sqrt(len(g)))


def draw_graph(g, k, a, b, show=False):
    nx.draw(g, pos=nx.fruchterman_reingold_layout(g), node_size=50, width=.1)
    plt.title("Force directed node layout for alpha: " + str(a) + " and beta: " + str(b))
    plt.savefig("graphs/graph-" + str(k) + "_alpha-" + str(a) + "_beta-" + str(b) + ".png")
    if show:
        plt.show()
    plt.clf()


def histogram(vals):
    plt.hist(vals)
    plt.show()
