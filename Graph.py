import Node

class Graph:
    def __init__(self,ex,wy):
        self.x=ex
        self.y=wy
        self.nodes=[]
        self.CreateNodes()
   
    def CreateNodes(self):
        i=0
        for j in range(0,self.x):
            for k in range(0,self.y):
                n=Node.Node(j,k,i)
                self.nodes.append(n)
                i+=1
    def write(strin):
        return