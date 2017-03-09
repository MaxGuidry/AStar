import Graph
import Node
import pickle

def GetNeighbors(node,graph):
    neighbors =[]
    if graph.nodes[node.identifier+graph.y] is not None:
        neighbors.append(graph.nodes[node.identifier+graph.y])
    if graph.nodes[node.identifier+1] is not None:
        neighbors.append(graph.nodes[node.identifier+1])
    if graph.nodes[node.identifier-graph.y] is not None:
        neighbors.append(graph.nodes[node.identifier-graph.y])
    if graph.nodes[node.identifier-1] is not None:
        neighbors.append(graph.nodes[node.identifier-1])
    return neighbors



testGraph = Graph.Graph(6,6)
testList = GetNeighbors(testGraph.nodes[15],testGraph)


