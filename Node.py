class Node:
    def __init__(self,d,g,ident):
        self.p=d
        self.y=g
        self.identifier=ident
    
    def print_info(self):
        s="Node:{} Value:\"{},{}\"".format(
            self.identifier,
            self.p,
            self.y
        )
        print s