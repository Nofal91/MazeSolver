from pyamaze import maze, COLOR, agent, textLabel
from timeit import timeit
from Dfs import dfs
from Bfs import BFS
from aStar import aStar
from getData import getData



k, l, algorithm, randMaze, searchPath, goalX, goalY = getData()



m=maze(k,l)
#m.CreateMaze(theme=COLOR.light)


goal=(goalX,goalY)

if randMaze:
    m.CreateMaze(goal[0],goal[1], loopPercent=50)
else:
    m.CreateMaze(goal[0],goal[1], loadMaze='mainMaze.csv')
    


# print(m.maze_map)

textLabel(m, 'Optimal path', 'Yellow')
textLabel(m, 'Optimal steps', len(m.path))
l2 = textLabel(m, 'search', 'Red')
l3 = textLabel(m, 'final path', 'Blue')



A_fwdPath, A_exploredPath = aStar(m, goal)
DFS_fwdPath, DFS_exploredPath = dfs(m, goal)
BFS_fwdpath, BFS_exploredPath = BFS(m, goal)





a = agent(m, footprints=True)
b = agent(m, footprints=True, color=COLOR.red, shape='arrow')
mainPath = agent(m, footprints=True, color=COLOR.yellow)


m.tracePath({mainPath:m.path}, delay=150)

if algorithm == "DFS": ##  DFS

    if searchPath : m.tracePath({b:DFS_exploredPath}, delay=200) #if the whole path needed
    m.tracePath({a:DFS_fwdPath}, delay=150)

elif algorithm == "BFS": ## BFS

    if searchPath : m.tracePath({b:BFS_exploredPath}, delay=200) #if the whole path needed
    m.tracePath({a:BFS_fwdpath},delay=150)

elif algorithm == "A*": ## A*

    if searchPath : m.tracePath({b:A_exploredPath},delay=200) #if the whole path needed
    m.tracePath({a:A_fwdPath},delay=150)



m.run()