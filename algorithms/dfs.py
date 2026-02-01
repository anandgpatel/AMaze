from utils.actions import actions
from utils.goal import goalMaze
from utils.cost import pathCost

#Algorithm - Depth first search (Stack)
def dfs(maze, start, goal):
    stack = [(start, [start], 0)]
    visitedStates = set()

    while stack:
        state, path, cost = stack.pop()

        if goalMaze(goal, state):
            return visitedStates, path, cost
    
        if state not in visitedStates:
            visitedStates.add(state)

            for nextState in actions(maze, state):
                stack.append((nextState, path + [nextState], pathCost(cost)))

    return None, None, None