"""Testing."""
import pygame
import astaralgorithm
import graph


def test_nodes():
    """Test the nodes."""
    g = graph.Graph([4, 4])
    node = astaralgorithm.get_node(4, g)
    node.print_info()
    neighbors = astaralgorithm.get_neighbors(node, g)
    for nod in neighbors:
        nod.print_info()


if __name__ == '__main__':
    testgraph = graph.Graph([10, 10])

    screen = pygame.display.set_mode((1080, 720))
    running = True
    circlepos = [540, 360]
    while running:
        pointsforgrid = []
        i = 0
        j = 0
        for n in range(0, (testgraph.x + 1) * (testgraph.y + 1)):
            pointsforgrid.append((i * 1080/testgraph.x, j * 720/testgraph.y))
            if j % 2 == 1:
                i -= 1
            else:
                i += 1
            if i > testgraph.x or i < 0:
                pygame.draw.aalines(screen, (255, 255, 255), True,
                                    pointsforgrid, 1)
                pointsforgrid = []
                j += 1
        i = 0
        j = testgraph.y
        pointsforgrid = []
        for n in range(0, (testgraph.x + 1) * (testgraph.y + 1)):
            pointsforgrid.append((i * 1080/testgraph.x, j * 720/testgraph.y))
            if i % 2 == 1:
                j += 1
            else:
                j -= 1
            if j > testgraph.y or j < 0:
                i += 1
                pygame.draw.aalines(screen, (255, 255, 255), True,
                                    pointsforgrid, 1)
                pointsforgrid = []
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    """Do a thing."""
        pygame.display.flip()
