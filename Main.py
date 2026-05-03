from pyamaze import maze, COLOR, agent, textLabel

from Dfs import dfs
from aStar import aStar

m=maze(15,15)
#m.CreateMaze(theme=COLOR.light)
m.CreateMaze(loopPercent=50,loadMaze='mainMaze.csv')
# print(m.maze_map)
textLabel(m, 'Optimal path', 'Yellow')
textLabel(m, 'Optimal steps', len(m.path))
l2 = textLabel(m, 'DFS search', 'Red')
l3 = textLabel(m, 'DFS final path', 'Blue')
A_fwdPath,A_exploredPath=aStar(m)
Dfs_fwdPath,Dfs_exploredPath=dfs(m)




a=agent(m,footprints=True)
b=agent(m,footprints=True,color=COLOR.red,shape='arrow')
mainPath=agent(m,footprints=True,color=COLOR.yellow)

#################
 # DFS

#m.tracePath({mainPath:m.path},delay=150)
# m.tracePath({b:dfsExplored},delay=200) #if the whole path needed
# m.tracePath({a:fwdPath},delay=150)

################
# A Star

m.tracePath({mainPath:m.path},delay=150)
m.tracePath({b:A_exploredPath},delay=100) #if the whole path needed
m.tracePath({a:A_fwdPath},delay=150)

m.run()