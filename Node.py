"""Node Class."""


class Node(object):
    """Node."""

    def __init__(self, d, g, ident):
        """D is x position and g is the y position ident is id of the Node."""
        self.p = d
        self.y = g
        self.identifier = ident

    def print_info(self):
        """Print all info of Node."""
        info = "Node:{} Value:\"{},{}\"".format(
            self.identifier,
            self.p,
            self.y
        )
        print info
