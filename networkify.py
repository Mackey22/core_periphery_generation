import networkx as nx


def networkify(adj):
    g = nx.Graph()

    d, _ = adj.shape

    for i in range(d):
        for j in range(i, d):
            if adj[i, j]:
                g.add_edge(i, j)
    return g
