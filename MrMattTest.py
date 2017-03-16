"""Testing."""
import pygame
import astar
import graph
import decimal

# all draw functions need to be reworked to fix decimal offset by pixels


def drawparents(screen, parents, currentgraph):
    for anode in parents:
        if anode.parent is not None:
            pygame.draw.line(screen, (255, 255, 255), (((screen.get_width() / currentgraph.width) * anode.posx) + (screen.get_width() / currentgraph.width) / 2, ((screen.get_height() / currentgraph.height) * anode.posy) + (screen.get_height() / currentgraph.height) / 2),
                             ((screen.get_width() / currentgraph.width) * anode.parent.posx + (screen.get_width() / currentgraph.width) / 2, ((screen.get_height() / currentgraph.height) * anode.parent.posy) + (screen.get_width() / currentgraph.width) / 2), 2)


def drawselected(screen, selectednode, currentgraph):
    offsetx = decimal.Decimal(decimal.Decimal(screen.get_width() % currentgraph.width) / currentgraph.width) * selectednode.posx
    offsety = decimal.Decimal(decimal.Decimal(screen.get_height() % currentgraph.height) / currentgraph.height) * selectednode.posy
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((screen.get_width() / currentgraph.width) *
                                                          selectednode.posx + offsetx, (screen.get_height() / currentgraph.height) * selectednode.posy + offsety, screen.get_width() / currentgraph.width, screen.get_height() / currentgraph.height), 5)


def drawstart(screen, startnode, currentgraph):
    offsetx = decimal.Decimal(decimal.Decimal(screen.get_width() % currentgraph.width) / currentgraph.width) * startnode.posx
    offsety = decimal.Decimal(decimal.Decimal(screen.get_height() % currentgraph.height) / currentgraph.height) * startnode.posy
    pygame.draw.rect(screen, (5, 230, 35), pygame.Rect((screen.get_width() / currentgraph.width) *
                                                       startnode.posx + offsetx, (screen.get_height() / currentgraph.height) * startnode.posy + offsety, screen.get_width() / currentgraph.width, screen.get_height() / currentgraph.height), 5)


def drawwalls(screen, walls, currentgraph):
    for wall in walls:
        offsetx = decimal.Decimal(decimal.Decimal(screen.get_width() % currentgraph.width) / currentgraph.width) * wall.posx
        offsety = decimal.Decimal(decimal.Decimal(screen.get_height() % currentgraph.height) / currentgraph.height) * wall.posy
        pygame.draw.rect(screen, (200, 50, 180), pygame.Rect((screen.get_width() / currentgraph.width) *
                                                            wall.posx + offsetx, (screen.get_height() / currentgraph.height) * wall.posy + offsety, screen.get_width() / currentgraph.width, screen.get_height() / currentgraph.height), 5)


def drawend(screen, endgoal, currentgraph):
    offsetx = decimal.Decimal(decimal.Decimal(screen.get_width() % currentgraph.width) / currentgraph.width) * endgoal.posx
    offsety = decimal.Decimal(decimal.Decimal(screen.get_height() % currentgraph.height) / currentgraph.height) * endgoal.posy
    pygame.draw.rect(screen, (16, 207, 236), pygame.Rect((screen.get_width() / currentgraph.width) *
                                                         endgoal.posx + offsetx, (screen.get_height() / currentgraph.height) * endgoal.posy + offsety, screen.get_width() / currentgraph.width, screen.get_height() / currentgraph.height), 5)


def drawpath(screen, path, currentgraph):
    for anode in path:
        offsetx = decimal.Decimal(decimal.Decimal(screen.get_width() % currentgraph.width) / currentgraph.width) * anode.posx
        offsety = decimal.Decimal(decimal.Decimal(screen.get_height() % currentgraph.height) / currentgraph.height) * anode.posy
        pygame.draw.rect(screen, (190, 0, 30), pygame.Rect((screen.get_width() / currentgraph.width) *
                                                            anode.posx + offsetx, (screen.get_height() / currentgraph.height) * anode.posy + offsety, screen.get_width() / currentgraph.width, screen.get_height() / currentgraph.height), 10)


if __name__ == '__main__':
    pygame.display.set_mode((1080, 720))
    SCREEN = pygame.display.get_surface()
    TESTGRAPH = graph.Graph([10, 10])
    for n in TESTGRAPH.nodes:
        TESTGRAPH.nodes[n].walkable = True
        TESTGRAPH.nodes[n].parent = None
        TESTGRAPH.nodes[n].g = 0
        TESTGRAPH.nodes[n].f = 0
        TESTGRAPH.nodes[n].h = 0
    RUNNING = True
    CURRENT = TESTGRAPH.nodes[0]
    ENDGOAL = TESTGRAPH.nodes[(TESTGRAPH.height * TESTGRAPH.width) - 1]
    SELECTED = TESTGRAPH.nodes[0]
    WALLS = []
    PATH = []
    TESTGRAPH.drawgraph(SCREEN)
    while RUNNING:
        EVENTS = pygame.event.get()
        for event in EVENTS:
            if event.type == pygame.KEYDOWN:
                pygame.display.set_mode((1080, 720))
                TESTGRAPH.drawgraph(SCREEN)
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False
                if event.key == pygame.K_RIGHT and SELECTED.identifier + TESTGRAPH.height < TESTGRAPH.height * TESTGRAPH.width:
                    SELECTED = TESTGRAPH.nodes[SELECTED.identifier +
                                               TESTGRAPH.height]
                if event.key == pygame.K_LEFT and SELECTED.identifier - TESTGRAPH.height > -1:
                    SELECTED = TESTGRAPH.nodes[SELECTED.identifier -
                                               TESTGRAPH.height]
                if event.key == pygame.K_DOWN and SELECTED.identifier < (TESTGRAPH.height * TESTGRAPH.width) - 1:
                    SELECTED = TESTGRAPH.nodes[SELECTED.identifier + 1]
                if event.key == pygame.K_UP and SELECTED.identifier > 0:
                    SELECTED = TESTGRAPH.nodes[SELECTED.identifier - 1]
                if event.key == pygame.K_c:
                    for n in TESTGRAPH.nodes:
                        TESTGRAPH.nodes[n].walkable = True
                        TESTGRAPH.nodes[n].parent = None
                        TESTGRAPH.nodes[n].g = 0
                        TESTGRAPH.nodes[n].f = 0
                        TESTGRAPH.nodes[n].h = 0
                    WALLS = []
                    PATH = []
                if event.key == pygame.K_w:
                    if TESTGRAPH.nodes[SELECTED.identifier] in WALLS:
                        WALLS.remove(TESTGRAPH.nodes[SELECTED.identifier])
                        TESTGRAPH.nodes[SELECTED.identifier].walkable = True
                    else:
                        TESTGRAPH.nodes[SELECTED.identifier].walkable = False
                        WALLS.append(TESTGRAPH.nodes[SELECTED.identifier])
                    #PATH = astar.astar(CURRENT, ENDGOAL)
                if event.key == pygame.K_s and SELECTED not in WALLS:
                    CURRENT = SELECTED
                if event.key == pygame.K_e and SELECTED not in WALLS:
                    ENDGOAL = SELECTED
                if event.key == pygame.K_SPACE:
                    PATH = astar.astar(CURRENT, ENDGOAL)
                if event.key == pygame.K_p:
                    PATH = []
       # drawparents(SCREEN, PATH, TESTGRAPH)
        if PATH is not None:
            drawpath(SCREEN, PATH, TESTGRAPH)
        drawwalls(SCREEN, WALLS, TESTGRAPH)
        drawselected(SCREEN, SELECTED, TESTGRAPH)
        drawstart(SCREEN, CURRENT, TESTGRAPH)
        drawend(SCREEN, ENDGOAL, TESTGRAPH)
        pygame.display.flip()
