from utils.actions import actions
from utils.goal import goalMaze
from utils.cost import pathCost
from collections import deque

#Algorithm - Breadth first search (Queue)
def bfs(maze, start, goal):
    queue = deque([(start, [start], 0)])
    visitedStates = set([start])

    while queue:
        state, path, cost = queue.popleft()

        if state not in visitedStates:
            visitedStates.add(state)

        if goalMaze(goal, state):
            return visitedStates, path, cost

        for nextState in actions(maze, state):
            if nextState not in visitedStates:
                queue.append((nextState, path + [nextState], pathCost(cost)))

    return None, None, None