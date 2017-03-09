import Node

class Graph:
    def __init__(self,xy):
        self.x=xy[0]
        self.y=xy[1]
        self.nodes={}
        self.CreateNodes()
   
    def CreateNodes(self):
        i=0
        for j in range(0,self.x):
            for k in range(0,self.y):
                n=Node.Node(j,k,i)
                self.nodes[n.identifier]=n
                i+=1
                
    