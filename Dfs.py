

from pyamaze import maze,textLabel




def dfs(m):

    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath = {}
    dfsExplored = []
    while len(frontier)>0:
        current=frontier.pop()
        dfsExplored.append(current)
        if current==(1,1):
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
                if child in explored:
                    continue
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=current
    l4=textLabel(m, 'Dfs steps', len(dfsExplored)-1)
    fwdPath={}
    goal=(1,1)
    while goal != start:
        fwdPath[dfsPath[goal]]=goal
        goal=dfsPath[goal]
    l5=textLabel(m, 'Dfs final path', len(fwdPath))
    return fwdPath,dfsExplored



