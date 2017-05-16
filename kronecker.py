# import networkx as nx
import numpy as np
import random
import copy


def make_kronecker(start_nodes=3, K=6, alpha=0.7, beta=0.4, c=0.15, d=0.05):
    # N = 3
    if start_nodes == 3:
        x = np.array([[alpha, alpha, beta], [alpha, alpha, alpha], [beta, alpha, alpha]])
        acc = np.array([[alpha, alpha, beta], [alpha, alpha, alpha], [beta, alpha, alpha]])
    elif start_nodes == 4:
        x = np.array([[1, alpha, beta, c], [alpha, 1, alpha, beta], [beta, alpha, 1, alpha], [c, beta, alpha, 1]])
        acc = np.array([[1, alpha, beta, c], [alpha, 1, alpha, beta], [beta, alpha, 1, alpha], [c, beta, alpha, 1]])
    elif start_nodes == 5:
        x = np.array([[1, alpha, beta, c, d], [alpha, 1, alpha, beta, c], [beta, alpha, 1, alpha, beta], [c, beta, alpha, 1, alpha], [d, c, beta, alpha, 1]])
        acc = np.array([[1, alpha, beta, c, d], [alpha, 1, alpha, beta, c], [beta, alpha, 1, alpha, beta], [c, beta, alpha, 1, alpha], [d, c, beta, alpha, 1]])

    # x = np.array([[alpha, alpha, beta], [alpha, alpha, alpha], [beta, beta, alpha]])
    # acc = np.array([[alpha, beta, beta], [alpha, alpha, alpha], [beta, beta, alpha]])

    # x = np.array([[alpha, beta], [beta, alpha]])
    # acc = np.array([[alpha, beta], [beta, alpha]])

    print 1, acc.shape, acc.shape[0]**2

    # P_k -> (19683 x 19683) -> 19683 nodes when k = 9
    # P_k -> 6561 nodes when k = 8
    # P_k -> 2187 nodes when k = 7
    # P_k -> 729 nodes when k = 6
    for i in range(K):
        acc = np.kron(acc, x)
        print i + 2, acc.shape, acc.shape[0]**2

    d, _ = acc.shape

    for i in range(d):
        for j in range(i, d):
            connected = 1 if acc[i, j] > random.random() else 0

            acc[i, j] = connected
            acc[j, i] = connected

            if i == j:
                acc[i, j] = 1
    return acc


def prune_graph(acc, growth, prior_d):
    # Remove unconnected nodes
    good_indices = np.any(acc > 0, axis=0)
    print acc.shape
    acc = acc[:, good_indices]
    acc = acc[good_indices, :]
    print acc.shape
    curr_size, _ = acc.shape

    prune_size = int(prior_d + prior_d * growth)
    if prior_d == prune_size:
        prune_size = prune_size + 1
    indices = np.random.choice(curr_size, prune_size, False)
    acc = acc[indices]
    acc = acc[:, indices]

    return acc


def iterative_kronecker(start_nodes, round, alpha=0.7, beta=0.4, c=0.15, d=0.05, acc=None, growth=0.5, default=0.005):
    # N = 3
    if start_nodes == 3:
        x = np.array([[alpha, alpha, beta], [alpha, alpha, alpha], [beta, alpha, alpha]])
    elif start_nodes == 4:
        x = np.array([[1, alpha, beta, c], [alpha, 1, alpha, beta], [beta, alpha, 1, alpha], [c, beta, alpha, 1]])
    elif start_nodes == 5:
        x = np.array([[1, alpha, beta, c, d], [alpha, 1, alpha, beta, c], [beta, alpha, 1, alpha, beta], [c, beta, alpha, 1, alpha], [d, c, beta, alpha, 1]])

    if acc is None:
        acc = copy.deepcopy(x)
    else:
        d, _ = acc.shape
        for i in range(d):
            for j in range(i, d):
                if acc[i, j] == 0:
                    acc[i, j] = default
                    acc[j, i] = default

    prior_d, _ = acc.shape

    acc = np.kron(acc, x)
    print round, acc.shape, acc.shape[0]**2

    d, _ = acc.shape

    for i in range(d):
        for j in range(i, d):
            connected = 1 if acc[i, j] > random.random() else 0

            acc[i, j] = connected
            acc[j, i] = connected

            if i == j:
                acc[i, j] = 0

    acc = prune_graph(acc, growth, prior_d)
    print "Pruned: ", round + 2, acc.shape, acc.shape[0]**2

    return acc
