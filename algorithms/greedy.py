from utils.actions import actions
from utils.goal import goalMaze
from utils.cost import pathCost
from utils.heuristic import heuristic
import heapq

#Algorithm - Greedy best first search
def greedy(maze, start, goal):
    priority = [(heuristic(start, goal), start, [start], 0)]
    visitedStates = set()

    while priority:
        _, state, path, cost = heapq.heappop(priority)

        if goalMaze(goal, state):
            return visitedStates, path, cost
        
        if state not in visitedStates:
            visitedStates.add(state)

            for nextState in actions(maze, state):
                h = heuristic(nextState, goal)
                heapq.heappush(priority, (h, nextState, path + [nextState], pathCost(cost)))

    return None, None, None