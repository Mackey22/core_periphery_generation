# import networkx as nx
import numpy as np
import random


def make_kronecker(K=6, alpha=0.7, beta=0.4, c=0.15, d=0.05):
    # N = 3

    # x = np.array([[alpha, alpha, beta], [alpha, alpha, alpha], [beta, alpha, alpha]])
    # acc = np.array([[alpha, alpha, beta], [alpha, alpha, alpha], [beta, alpha, alpha]])

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
