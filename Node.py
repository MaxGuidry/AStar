"""Node Class."""


class Node(object):
    """Node."""

    def __init__(self, d, g, ident):
        """D is x position and g is the y position ident is id of the Node."""
        self.posx = d
        self.posy = g
        self.walkable = True
        self._gcost = 0
        self._hcost = 0
        self._fcost = 0
        self.parent = None
        self.neighbors = []
        self.identifier = ident

    @property
    def h(self):
        return self._hcost

    @h.setter
    def h(self, value):
        self._hcost = value
    
    @property
    def g(self):
        return self._gcost

    @g.setter
    def g(self, value):
        self._gcost = value

    @property
    def f(self):
        return self._fcost

    @f.setter
    def f(self, value):
        self._fcost = value