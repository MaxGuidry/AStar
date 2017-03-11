import Graph
import Node
import pickle
import AStarAlgorithm

TESTGRAPH = Graph.Graph(12, 12)
start = TESTGRAPH.GetNode(0)
end = TESTGRAPH.GetNode(12)
current = start

AStarAlgorithm.AStar()

testList = GetNeighbors(TESTGRAPH.nodes[34], TESTGRAPH)
pickle.dump(TESTGRAPH, open("Graph.txt", 'wb'), protocol=2)
testing = pickle.load(open("Graph.txt", 'rb'))
