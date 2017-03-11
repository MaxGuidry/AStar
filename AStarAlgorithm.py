"""Astar Algorithm."""
import node


def get_node(index, g):
    """Get node with given index in the given graph."""
    if index in g.nodes:
        return g.nodes[index]
    else:
        return None


open = []
closed = []

start = node.Node(0, 0, 0)


def get_neighbors(n, g):
    """Get neighbors of given node in the given graph."""
    neighbors = []

    right = get_node(n.identifier + g.y, g)
    up = get_node(n.identifier + 1, g)
    left = get_node(n.identifier - g.y, g)
    down = get_node(n.identifier - 1, g)
    if right is not None:
        neighbors.append(right)
    if up is not None and n.identifier % g.y != g.y - 1:
        neighbors.append(up)
    if left is not None:
        neighbors.append(left)
    if down is not None and n.identifier % g.y != 0:
        neighbors.append(down)
    return neighbors
