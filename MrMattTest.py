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
    screen = pygame.display.set_mode((900, 900))
    running = True

    pygame.draw.circle(screen, (255, 255, 255), (900, 900), 100, 0)
    pygame.display.flip()

    pygame.event.get()
