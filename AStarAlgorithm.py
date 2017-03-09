import Graph
import Node


def GetNode(index, g):
    if g.nodes.has_key(index):
        return g.nodes[index]
    else:
        return None


open = []
start = Node.Node(0, 0, 0)


def GetNeighbors(node, graph):
    neighbors = []

    right = GetNode(node.identifier + graph.y, graph)
    up = GetNode(node.identifier + 1, graph)
    left = GetNode(node.identifier - graph.y, graph)
    down = GetNode(node.identifier - 1, graph)
    if right is not None:
        neighbors.append(right)
    if up is not None and node.identifier % graph.y != graph.y - 1:
        neighbors.append(up)
    if left is not None:
        neighbors.append(left)
    if down is not None and node.identifier % graph.y != 0:
        neighbors.append(down)
    return neighbors
