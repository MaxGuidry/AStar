'''Hello World.'''


def retrace(start, endnode):
    """Retracing path from goal to start."""
    path = []
    itera = endnode
    while itera is not None:
        path.append(itera)
        itera = itera.parent
    return path


def dist(current, next):
    """Estimates the distance."""
    return 10 if current.posx == next.posx or current.posy == next.posy else 14


def mhdm(nodetotest, goal):
    x = abs(goal.posx - nodetotest.posx) 
    y = abs(goal.posy - nodetotest.posy)
    if x > y:
        return (y * 14) + (x-y) * 10
    if y > x:
        return (x * 14) + (y-x) * 10
    else:
        return x * 14
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
    while len(open) != 0:
        open = sorted(open, key=lambda x: x.f)
        current = open[0]
        open.remove(current)
        closed.append(current)
        if current == goal:
            camefrom = retrace(start, current)
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
            n.h = mhdm(n, goal)
            n.f = n.g + n.h
