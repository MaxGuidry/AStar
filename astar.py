'''Hello World.'''


def retrace(endnode):
    '''Retrace path from goal to start.'''
    path = []
    while endnode is not None:
        path.append(endnode)
        endnode = endnode.parent
    return path


def dist(current, next):
    """Estimates the distance."""
    return 10 if current.posx == next.posx or current.posy == next.posy else 14


def mhd(nodetotest, goal):
    return (abs(goal.posx - nodetotest.posx) + abs(goal.posy - nodetotest.posy)) * 10


def astar(start, goal):
    camefrom = []
    closed = []
    open = []
    start.h = 0
    start.g = 0
    start.f = start.g + start.h
    open.append(start)  
    while open is not None:
        open = sorted(open, key=lambda x: x.f)
        current = open[0]
        open.remove(current)
        closed.append(current)
        if current == goal:
            camefrom = retrace(current)
            return camefrom
        for n in current.neighbors:
            if n in closed or n.walkable is False:
                continue
            tentative_g = current.g + dist(current, n)
            if n not in open:
                open.append(n)
            elif tentative_g >= n.g:
                continue
            n.parent = current
            n.g = tentative_g
            n.h = mhd(n,goal)
            n.f = n.g + n.h
