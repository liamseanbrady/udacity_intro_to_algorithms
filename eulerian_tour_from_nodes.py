def create_tour(nodes):
    # your code here
    firstNode = nodes[0]
    numNodes = len(nodes)
    i = 0
    edgeList = []
    while i < numNodes - 1:
        edgeList.append((nodes[i], nodes[i+1]))
        i = i + 1
    edgeList.append((nodes[numNodes-1], firstNode))
    return edgeList