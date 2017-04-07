"""Graph Class."""
import node
import pygame
import helpers
class Graph(object):
    """Graph."""

    def __init__(self, xy):
        """Contructor xy is a list of dimensions."""
        self.width = xy[0]
        self.height = xy[1]
        self.nodes = {}
        self.createnodes()

    def createnodes(self):
        """Function to Create all the nodes."""
        i = 0
        for j in range(0, self.width):
            for k in range(0, self.height):
                n = node.Node(j, k, i)
                self.nodes[int(n.guid)] = n
                i += 1
        for nds in self.nodes:
            self.nodes[nds].walkable = True
            self.nodes[nds].neighbors = helpers.get_neighbors(self.nodes[nds], self)