"""Graph Class."""
import node


class Graph(object):
    """Graph."""

    def __init__(self, xy):
        """Contructor xy is a list of dimensions."""
        self.x = xy[0]
        self.y = xy[1]
        self.nodes = {}
        self.createnodes()

    def createnodes(self):
        """Function to Create all the nodes."""
        i = 0
        for j in range(0, self.x):
            for k in range(0, self.y):
                n = node.Node(j, k, i)
                self.nodes[n.identifier] = n
                i += 1
