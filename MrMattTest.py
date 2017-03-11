"""Testing."""
import pygame
import astaralgorithm
import graph


def test_nodes():
    """Test the nodes."""
    testgraph = graph.Graph([4, 4])
    node = astaralgorithm.get_node(4, testgraph)
    node.print_info()
    neighbors = astaralgorithm.get_neighbors(node, testgraph)
    for nod in neighbors:
        nod.print_info()


if __name__ == '__main__':
    TESTGRAPH = graph.Graph([10, 10])

    SCREEN = pygame.display.set_mode((1080, 720))
    RUNNING = True
    while RUNNING:
        POINTSFORGRID = []
        i = 0
        j = 0
        for n in range(0, (TESTGRAPH.x + 1) * (TESTGRAPH.y + 1)):
            POINTSFORGRID.append((i * SCREEN.get_width()/TESTGRAPH.x, j *
                                  SCREEN.get_height()/TESTGRAPH.y))
            if j % 2 == 1:
                i -= 1
            else:
                i += 1
            if i > TESTGRAPH.x or i < 0:
                pygame.draw.aalines(SCREEN, (255, 255, 255), True,
                                    POINTSFORGRID, 1)
                POINTSFORGRID = []
                j += 1
                i = 0 if i < 0 else i-1
        i = 0
        j = TESTGRAPH.y
        POINTSFORGRID = []
        for n in range(0, (TESTGRAPH.x + 1) * (TESTGRAPH.y + 1)):
            POINTSFORGRID.append((i * SCREEN.get_width()/TESTGRAPH.x, j *
                                  SCREEN.get_height()/TESTGRAPH.y))
            if i % 2 == 1:
                j += 1
            else:
                j -= 1
            if j > TESTGRAPH.y or j < 0:
                i += 1
                pygame.draw.aalines(SCREEN, (255, 255, 255), True,
                                    POINTSFORGRID, 1)
                POINTSFORGRID = []
                j = 0 if j < 0 else j-1
        EVENTS = pygame.event.get()
        for event in EVENTS:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False
        pygame.display.flip()
