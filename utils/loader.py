#Load maze from text file
def loadMaze(file_name):
    maze = []
    start = goal = None

    #Open text file and read contents
    with open (file_name, "r") as file:
        for row, line in enumerate(file):
            data = list(line.rstrip("\n"))
            maze.append(data)

            for column, ch in enumerate(data):
                #Locate starting point
                if ch == "A":
                    start = (row, column)
                #Locate ending point
                elif ch == "Z":
                    goal = (row, column)

    return maze, start, goal