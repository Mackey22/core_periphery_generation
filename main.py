from kronecker import make_kronecker
from networkify import networkify
from analysis import do_some_analysis
from draw import draw_graph


def do_everything(k, a, b):
    adj = make_kronecker(K=k)
    g = networkify(adj)
    do_some_analysis(g, k, a, b)
    draw_graph(g, k, a, b)

if __name__ == "__main__":
    # do_everything(5, .8, 0)
    # do_everything(5, .5, .5)
    do_everything(3, .7, .25)
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
