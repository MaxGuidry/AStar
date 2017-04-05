"""Astar Algorithm."""
import node


def get_node(index, g):
    """Get node with given index in the given graph."""
    # if index in g.nodes and index >= 0:
    #     return g.nodes[index]
    # else:
    #     return None
    if index < 99 and index > 0:
        return g[index]


def get_neighbors(n, g):
    """Get neighbors of given node in the given graph."""
    neighbors = []

    right = get_node(int(n.guid) + 10, g)
    upper = get_node(int(n.guid) - 1, g)
    left = get_node(int(n.guid) - 10, g)
    down = get_node(int(n.guid) + 1, g)
    upright = get_node(int(n.guid) + 10 - 1, g)
    downright = get_node(int(n.guid) + 10 + 1, g)
    upleft = get_node(int(n.guid) - 10 - 1, g)
    downleft = get_node(int(n.guid) - 10 + 1, g)
    if right is not None:
        neighbors.append(right)
    if upright is not None and int(n.guid) % 10 != 0:
        neighbors.append(upright)
    if upper is not None and int(n.guid) % 10 != 0:
        neighbors.append(upper)
    if upleft is not None and int(n.guid) % 10 != 0:
        neighbors.append(upleft)
    if left is not None:
        neighbors.append(left)
    if downleft is not None and int(n.guid) % 10 != 10 - 1:
        neighbors.append(downleft)
    if down is not None and int(n.guid) % 10 != 10 - 1:
        neighbors.append(down)
    if downright is not None and int(n.guid) % 10 != 10 - 1:
        neighbors.append(downright)
    return neighbors
