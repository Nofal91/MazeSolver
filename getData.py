


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
        x=15
        y=15
    



    z = int(input("Choose your search algorithm 1.DFS 2.BFS 3.A* : "))

    
    

    goalCheck = False

    while goalCheck == False :
    
        goal_input = input("Enter the goal target x,y :")

        goalParts = goal_input.split(',')


        goalX = int(goalParts[0])
        goalY = int(goalParts[1])

        if goalX > x or goalY > y or goalX < 1 or goalY < 1:
            print("Goal is not on the map try again !")
        else:
            goalCheck = True

    
    




    path_input = int(input("Do you want to see the search Paths 1.Yes 2.No : "))

    if path_input == 1:
        path = True
    else:
        path = False



    if z == 1:
        searchAlgorithm = 'DFS'
    elif z == 2:
        searchAlgorithm = 'BFS'
    elif z == 3:
        searchAlgorithm = 'A*'
    else:
        searchAlgorithm = None




    return x,y,searchAlgorithm,RandMaze, path, goalX, goalY