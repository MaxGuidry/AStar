"""Graph Class."""
import node
import pygame
import AStarAlgorithm
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
            self.nodes[nds].neighbors = AStarAlgorithm.get_neighbors(self.nodes[nds], self)
    def drawgraph(self,SCREEN):
        POINTSFORGRID = []
        i = 0
        j = 0
        for n in range(0, (self.width + 1) * (self.height + 1)):
            POINTSFORGRID.append((i * SCREEN.get_width()/self.width, j *
                                  SCREEN.get_height()/self.height))
            if j % 2 == 1:
                i -= 1
            else:
                i += 1
            if i > self.width or i < 0:
                pygame.draw.aalines(SCREEN, (255, 255, 255), True,
                                    POINTSFORGRID, 1)
                POINTSFORGRID = []
                j += 1
                i = 0 if i < 0 else i-1
        i = 0
        j = self.height
        POINTSFORGRID = []
        for n in range(0, (self.width + 1) * (self.height + 1)):
            POINTSFORGRID.append((i * SCREEN.get_width()/self.width, j *
                                  SCREEN.get_height()/self.height))
            if i % 2 == 1:
                j += 1
            else:
                j -= 1
            if j > self.height or j < 0:
                i += 1
                pygame.draw.aalines(SCREEN, (255, 255, 255), True,
                                    POINTSFORGRID, 1)
                POINTSFORGRID = []
                j = 0 if j < 0 else j-1