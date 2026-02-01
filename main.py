from utils.loader import loadMaze
from utils.htmlRenderer import solvedMaze
from algorithms.dfs import dfs
from algorithms.bfs import bfs
from algorithms.greedy import greedy
from algorithms.astar import astar


#Main function
def main():
    maze, start, goal = loadMaze("maze.txt")

    choice = input("======= AMaze =======\n\n1. Deep first search (Stack)\n2. Breadth first search (Queue)\n3. Greedy best first search\n4. A star\n0. Exit\n\nEnter your choice (1, 2, 3, 4 or 0): ")

    if choice == "1":
        algorithm = "Deep first search (Stack)"
        visitedStates, path, cost = dfs(maze, start, goal)
    elif choice == "2":
        algorithm = "Breadth first search (Queue)"
        visitedStates, path, cost = bfs(maze, start, goal)
    elif choice == "3":
        algorithm = "Greedy best first search"
        visitedStates, path, cost = greedy(maze, start, goal)
    elif choice == "4":
        algorithm = "A star"
        visitedStates, path, cost = astar(maze, start, goal)
    elif choice == "0":
        return
    else:
        raise ValueError("Invalid choice!")
    
    solvedMaze(maze, visitedStates, path, algorithm, cost)

if __name__ == "__main__":
    main()