from pyamaze import maze, COLOR, agent, textLabel

from Dfs import dfs


m=maze(10,10)
#m.CreateMaze(theme=COLOR.light)
m.CreateMaze(loopPercent=20)
# print(m.maze_map)

fwdPath,dfsExplored=dfs(m)



a=agent(m,filled=True,footprints=True)
b=agent(m,footprints=True,color=COLOR.red,shape='arrow')
mainPath=agent(m,footprints=True,color=COLOR.yellow)



m.tracePath({mainPath:m.path},delay=100)
m.tracePath({b:dfsExplored},delay=100) #if the whole path needed
m.tracePath({a:fwdPath},delay=100)

m.run()