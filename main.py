import numpy as np

from kronecker import make_kronecker, iterative_kronecker
from networkify import networkify
from analysis import do_some_analysis, draw_graph


def make_clans(dim):
    adj = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(i, dim):
            if j - i < 10 and (j / 10 == i / 10):
                adj[i, j] = 1
                adj[j, i] = 1
    return adj


def make_generation(i, a, b, c, d, start_nodes, prev_adj):
    adj = iterative_kronecker(start_nodes, i, a, b, c, d, prev_adj)
    g = networkify(adj)
    do_some_analysis(g, i, a, b, c, d)
    draw_graph(g, i, a, b, c, d)
    return adj


def everything_iterative(a, b, start_nodes, c=None, d=None):
    CLANS = True

    if CLANS:
        prev_adj = make_clans(50)
        g = networkify(prev_adj)
        draw_graph(g, -1, a, b, c, d)
        i = 0
    else:
        prev_adj = make_generation(0, a, b, c, d, start_nodes, None)
        i = 1

    while len(prev_adj) < 800:
        prev_adj = make_generation(i, a, b, c, d, start_nodes, prev_adj)
        i += 1


def do_everything(k, a, b, c=None, d=None):
    adj = make_kronecker(K=k)
    g = networkify(adj)
    do_some_analysis(g, k, a, b, c, d)
    draw_graph(g, k, a, b, c, d)

if __name__ == "__main__":
    # do_everything(5, .8, 0)
    # do_everything(5, .5, .5)
    everything_iterative(.8, .6, 3, c=.4, d=.2)
    # do_everything(5, 1, .8)
    # do_everything(5, 1, 0.7)
    # do_everything(5, 1, 0)
    # do_everything(5, .9, .1)
    # for k in range(8):
    #     for b in range(10):
    #         beta = float(b) / 10
    #         for a in range(b, 10):
    #             alpha = float(a) / 10
    #             do_everything(k, alpha, beta)
