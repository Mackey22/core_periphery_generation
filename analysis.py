import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def sort_dict_by_val(d):
    """Get a list of a dict's keys ordered by descending values."""
    return sorted(d, key=d.__getitem__, reverse=True)


def make_title(a, b, c, d):
    title = "Force directed node layout for alpha: " + str(a) + ", beta: " + str(b)
    if c is not None:
        title += ", gamma: " + str(c)
    if d is not None:
        title += ", rho: " + str(d)
    return title


def make_name(k, a, b, c, d):
    name = "alpha-" + str(a) + "_beta-" + str(b)
    if c is not None:
        name += "_gamma-" + str(c)
    if d is not None:
        name += "_rho-" + str(d)
    return name + "_i-" + str(k) + ".png"


def draw_graph(g, k, a, b, c, d, show=False):
    nx.draw(g, pos=nx.fruchterman_reingold_layout(g), node_size=50, width=.1)
    title = make_title(a, b, c, d)
    plt.title(title)
    name = make_name(k, a, b, c, d)
    plt.savefig("graphs3/" + name)
    if show:
        plt.show()
    plt.clf()


def do_some_analysis(g, k, a, b, c, d, show=False):
    centrality = nx.closeness_centrality(g)

    values = sorted(centrality.values(), reverse=True)

    num_bins = 50

    fig, ax = plt.subplots()
    hist, bins = np.histogram(values, bins=num_bins)
    # print hist
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.ylabel("Number of Nodes")
    plt.xlabel("Closeness Centrality")

    title = make_title(a, b, c, d)
    plt.title(title)

    name = make_name(k, a, b, c, d)
    plt.savefig("hist2/" + name)
    if show:
        plt.show()
    plt.clf()
