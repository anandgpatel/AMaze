from utils.actions import actions
from utils.goal import goalMaze
from utils.cost import pathCost
from utils.heuristic import heuristic
import heapq

#Algorithm - A star
def astar(maze, start, goal):
    priority = [(0 + heuristic(start, goal), 0, start, [start])]
    visitedStates = {}

    while priority:
        gPlusH, cost, state, path = heapq.heappop(priority)

        if goalMaze(goal, state):
            return visitedStates, path, cost
        
        if state not in visitedStates or cost < visitedStates[state]:
            visitedStates[state] = cost

            for nextState in actions(maze, state):
                newCost = pathCost(cost)
                newGPlusH = newCost + heuristic(nextState, goal)
                heapq.heappush(priority, (newGPlusH, newCost, nextState, path + [nextState]))

    return None, None, None