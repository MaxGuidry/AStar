import pygame
import AStarAlgorithm
import Node
import Graph

def test_nodes():
    '''test the nodes'''
    graph = Graph.Graph([3, 3])
    node = AStarAlgorithm.GetNode(4, graph)
    node.print_info()
    neighbors = AStarAlgorithm.GetNeighbors(node, graph)
    for nod in neighbors:
        nod.print_info()



if __name__ == '__main__':
    test_nodes()
    pygame.display.set_mode((900,900))
    for x in range(0,213400000):        
        pygame.display.flip()
        pygame.draw.circle(pygame.Surface.Surface(width,height),(255,255,255),4,width=0)

        pygame.event.get()
    