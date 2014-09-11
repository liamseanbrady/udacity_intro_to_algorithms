import random

def create_random_tour(nodes):
    edges = []
    outerRand = random.randrange(0, len(nodes))
    stored = nodes[outerRand]
    del nodes[outerRand]
    while len(nodes) >= 1:
        innerRand = random.randrange(0, len(nodes))
        secondNode = nodes[innerRand]
        del nodes[innerRand]
        edge = (stored, secondNode)
        edges.append(edge)
        stored = secondNode
    lastEdge = (edges[len(edges)-1][1], edges[0][0])
    edges.append(lastEdge)
    return edges

def random_tour_test():
    nodes = [20, 21, 22, 23, 24, 25]
    tour = create_random_tour(nodes)
    return tour