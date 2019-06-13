# Uses python3

import sys
from collections import deque


def add_edge(graph, vertex, vertex2):
    """Builds adge of a graph by adding vertex 2 in adjacent list of vertex 1.

    If the vertex(key) does not exist in the graph(dictionary), the vertex is 
    constructed.


    Parameters
    ----------
    graph: dictionary
        The graph being constructed as an adjacency list
    vertex1, vertex2: int
        vertex1 is the key and vertex 2 is the neighbour to be added to vertex1
        list
    """

    edges = (vertex, vertex2)
    (v1, v2) = (edges)
    if v1 in graph:
        if v2 not in graph[v1]:
            graph[v1].append(v2)
            graph[v2].append(v1)
        else:
            graph[v1] = v2


def distance(adj, s, t):
    #write your code here
    return -1


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2)

    start, end = map(int, sys.stdin.readline().split())
    print(graph)

    # print(distance(adj, s, t))
