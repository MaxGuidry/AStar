'''Hello World.'''
import helpers as get
import testastar as tas



def retrace(start, endnode):
    """Retracing path from goal to start."""
    path = []
    itera = endnode
    while itera is not start:
        path.append(itera)
        itera = itera.parent
    path.append(itera)
    return path


def dist(current, next):
    """Estimates the distance."""
    return 10 if current.pos[0] == next.pos[0] or current.pos[1] == next.pos[1] else 14


def mhdm(nodetotest, goal):
    x = abs(goal.pos[0] - nodetotest.pos[0]) 
    y = abs(goal.pos[1] - nodetotest.pos[1])
    if x > y:
        return (y * 14) + (x-y) * 10
    if y > x:
        return (x * 14) + (y-x) * 10
    else:
        return x * 14
def mhd(nodetotest, goal):
    return (abs(goal.pos[0] - nodetotest.pos[0]) + abs(goal.pos[1] - nodetotest.pos[1])) * 10

def astar(start, goal, graph):
    camefrom = []
    closed = []
    open = []
    start.h = 0
    start.g = 0
    start.f = start.g + start.h
    open.append(start)  
    open = sorted(open, key=lambda x: x.f)

    while len(open) != 0:
        current = open[0]
        open.remove(current)
        closed.append(current)
        if current == goal:
            camefrom = retrace(start, current)
            return camefrom
        neighbors = tas.getneighbors(current, graph)
        for n in neighbors:
            if n in closed or n.walkable is False:
                continue
            tentative_g = current.g + dist(current, n)
            if n not in open:
                open.append(n)
            elif tentative_g >= n.g:
                continue
            n.parent = current
            n.g = tentative_g
            n.h = mhd(n, goal)
            n.f = n.g + n.h
    return camefrom
