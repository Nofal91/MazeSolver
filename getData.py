


def getData():

    

    Maze = int(input("Do you want to use a random maze 1.Yes 2.No : "))

    if Maze == 1:


        user_input = input("Enter the size of the maze that you want x,y : ")

        parts = user_input.split(',')

        x = int(parts[0])
        y = int(parts[1])

        RandMaze = True
    else:
        
        RandMaze = False
        x=10
        y=10
    



    z = int(input("Choose your search algorithm 1.DFS 2.BFS 3.A* 4.Dijkstra : "))




    if z == 1:
        searchAlgorithm = 'DFS'
    elif z == 2:
        searchAlgorithm = 'BFS'
    elif z == 3:
        searchAlgorithm = 'A*'
    elif z == 4:
        searchAlgorithm = 'Dijkstra'
    else:
        searchAlgorithm = None




    return x,y,searchAlgorithm,RandMaze