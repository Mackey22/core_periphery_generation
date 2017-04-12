import networkx as nx
from draw import histogram
import matplotlib.pyplot as plt
import numpy as np


def sort_dict_by_val(d):
    """Get a list of a dict's keys ordered by descending values."""
    return sorted(d, key=d.__getitem__, reverse=True)


def do_some_analysis(g, k, a, b, show=False):
    centrality = nx.closeness_centrality(g)

    values = sorted(centrality.values(), reverse=True)

    num_bins = 50

    fig, ax = plt.subplots()
    hist, bins = np.histogram(values, bins=num_bins)
    print hist
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.ylabel("Number of Nodes")
    plt.xlabel("Closeness Centrality")
    plt.title("Centrality for alpha: " + str(a) + " and beta: " + str(b))

    plt.savefig("graphs/hist-" + str(k) + "_alpha-" + str(a) + "_beta-" + str(b) + ".png")
    if show:
        plt.show()
    plt.clf()
