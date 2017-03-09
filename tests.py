import Graph
import Node
import pickle
import AStarAlgorithm

testGraph = Graph.Graph(12,12)
start = testGraph.GetNode(0)
end = testGraph.GetNode(12)
current =start

AStarAlgorithm.AStar()

testList = GetNeighbors(testGraph.nodes[34],testGraph)
pickle.dump(testGraph,open("Graph.txt",'wb'),protocol=2)
testing = pickle.load(open("Graph.txt",'rb'))

