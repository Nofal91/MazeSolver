from pyamaze import textLabel
from queue import PriorityQueue



def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2)+abs(y1-y2)



def aStar(m,g):
    start=(m.rows,m.cols)
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start,g)

    q = PriorityQueue()

    q.put((h(start, g), h(start, g), start))
    aPath = {}
    aExplored = []
    while not q.empty():
        current = q.get()[2]
        aExplored.append(current)
        if current==g:
            break
        for d in 'ESNW':
            if m.maze_map[current][d]==True:
                if d == 'E':
                    child=(current[0],current[1]+1)
                elif d == 'W':
                    child=(current[0],current[1]-1)
                elif d == 'N':
                    child=(current[0]-1,current[1])
                elif d == 'S':
                    child=(current[0]+1,current[1])
                new_g_score = g_score[current] + 1
                new_f_score = new_g_score + h(child, g)
                if new_f_score < f_score[child]:
                    f_score[child] = new_f_score
                    g_score[child] = new_g_score
                    q.put((new_f_score, h(child,g), child))
                    aPath[child]=current
    l4 = textLabel(m, 'A* steps', len(aExplored) - 1)
    fwdPath = {}
    goal = g
    while goal != start:
        fwdPath[aPath[goal]]=goal
        goal=aPath[goal]
    l5 = textLabel(m, 'A* final path', len(fwdPath))
    return fwdPath,aExplored

