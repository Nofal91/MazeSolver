from pyamaze import maze, COLOR, agent, textLabel
from timeit import timeit
from Dfs import dfs
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
l2 = textLabel(m, 'DFS search', 'Red')
l3 = textLabel(m, 'DFS final path', 'Blue')


A_fwdPath, A_exploredPath = aStar(m, goal)
Dfs_fwdPath, Dfs_exploredPath = dfs(m, goal)




a = agent(m, footprints=True)
b = agent(m, footprints=True, color=COLOR.red, shape='arrow')
mainPath = agent(m, footprints=True, color=COLOR.yellow)



if algorithm == "DFS": ##  DFS

    m.tracePath({mainPath:m.path}, delay=150)
    if searchPath : m.tracePath({b:Dfs_exploredPath}, delay=200) #if the whole path needed
    m.tracePath({a:Dfs_fwdPath}, delay=150)

elif algorithm == "BFS": ## BFS

    print("Under Construction")


elif algorithm == "A*": ## A*

    m.tracePath({mainPath:m.path},delay=150)
    if searchPath : m.tracePath({b:A_exploredPath},delay=200) #if the whole path needed
    m.tracePath({a:A_fwdPath},delay=150)



m.run()