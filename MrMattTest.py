"""Testing."""
import pygame
import astar
import graph


def drawselected(screen, selectednode,currentgraph):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((screen.get_width()/currentgraph.width) * selectednode.identifier & currentgraph.width, (screen.get_height()/currentgraph.height) * selectednode.identifier % currentgraph.height, screen.get_width() / currentgraph.width, screen.get_height() / currentgraph.height), 0)

if __name__ == '__main__':
    pygame.display.set_mode((1080, 720))
    SCREEN = pygame.display.get_surface()
    TESTGRAPH = graph.Graph([35, 35])
    TESTGRAPH.drawgraph(SCREEN)
    TESTGRAPH.nodes[3].walkable = False
    TESTGRAPH.nodes[13].walkable = False
    TESTGRAPH.nodes[23].walkable = False
    TESTGRAPH.nodes[33].walkable = False
    TESTGRAPH.nodes[32].walkable = False
    TESTGRAPH.nodes[31].walkable = False
    test1 = astar.astar(TESTGRAPH.nodes[0], TESTGRAPH.nodes[44])

    for n in TESTGRAPH.nodes:
        TESTGRAPH.nodes[n].walkable = True
        TESTGRAPH.nodes[n].parent = None
        TESTGRAPH.nodes[n].g = 0
        TESTGRAPH.nodes[n].f = 0
        TESTGRAPH.nodes[n].h = 0

    TESTGRAPH.nodes[21].walkable = False
    TESTGRAPH.nodes[22].walkable = False
    TESTGRAPH.nodes[23].walkable = False
    test2 = astar.astar(TESTGRAPH.nodes[2], TESTGRAPH.nodes[42])

    for n in TESTGRAPH.nodes:
        TESTGRAPH.nodes[n].walkable = True
        TESTGRAPH.nodes[n].parent = None
        TESTGRAPH.nodes[n].g = 0
        TESTGRAPH.nodes[n].f = 0
        TESTGRAPH.nodes[n].h = 0

    TESTGRAPH.nodes[33].walkable = False
    TESTGRAPH.nodes[32].walkable = False
    TESTGRAPH.nodes[34].walkable = False
    TESTGRAPH.nodes[42].walkable = False
    TESTGRAPH.nodes[44].walkable = False
    TESTGRAPH.nodes[52].walkable = False
    TESTGRAPH.nodes[54].walkable = False
    TESTGRAPH.nodes[62].walkable = False
    TESTGRAPH.nodes[64].walkable = False
    test3 = astar.astar(TESTGRAPH.nodes[3], TESTGRAPH.nodes[53])
    RUNNING = True
    CURRENT = TESTGRAPH.nodes[0]
    ENDGOAL = TESTGRAPH.nodes[(TESTGRAPH.height * TESTGRAPH.width) - 1]
    SELECTED = TESTGRAPH.nodes[0]
    while RUNNING:
        drawselected(SCREEN, CURRENT, TESTGRAPH)
        EVENTS = pygame.event.get()
        for event in EVENTS:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False
                if event.type == pygame.K_SPACE:
                    path = astar.astar(current, endgoal)
        pygame.display.flip()
