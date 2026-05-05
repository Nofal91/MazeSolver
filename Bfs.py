
from pyamaze import textLabel




def BFS(m, goal):

    start = (m.rows, m.cols)

    explored = [start]
    frontier = [start]

    bfsPath = {}
    bfsExplored = []

    while len(frontier)>0:

        currCell = frontier.pop(0)
        bfsExplored.append(currCell)

        if currCell == goal : break
        
        for d in 'ESNW':

            if m.maze_map[currCell][d]==True:
                if d == 'E':
                    child = (currCell[0], currCell[1]+1)
                elif d == 'S':
                    child = (currCell[0]+1, currCell[1])
                elif d == 'N':
                    child = (currCell[0]-1, currCell[1])
                elif d == 'W':
                    child = (currCell[0], currCell[1]-1)

                if child in explored: continue

                frontier.append(child)
                explored.append(child)
                bfsPath[child] = currCell

    l4=textLabel(m, 'BFS steps', len(bfsExplored)-1)
    
    fwdpath={}

    cell = goal

    while cell != start:
        fwdpath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    
    l5=textLabel(m, 'BFS final path', len(fwdpath))

    return fwdpath, bfsExplored
                




















