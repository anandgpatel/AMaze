# Maze Solver Using AI Search Algorithms
This project is a Python-based maze solver that uses classical Artificial Intelligence search algorithms to find a path from a start point to a goal. The solution is visualized in a web browser using an automatically generated HTML file.

# Algorithms Implemented
- Depth first search (Stack)
- Breadth first search (Queue)
- Greedy best first Search
- A star search

# How It Works
- The maze is loaded from a text file ("maze.txt")
- The user selects a search algorithm from the command line menu
- The selected algorithm explores the maze using appropriate data structures
- The final path and all visited nodes are visualized in an HTML page
- The HTML file opens automatically in the browser after execution

# Project Structure
```text
AMaze/
│
├── algorithms/
│   ├── astar.py
│   ├── bfs.py
│   ├── dfs.py
│   └── greedy.py
│
├── utils/
│   ├── actions.py
│   ├── cost.py
│   └── goal.py
│   └── heuristic.py
│   └── htmlRenderer.py
│   └── loader.py
│
├── maze.txt
├── main.py
└── README.md
```

# Prerequisites
- Python 3.8 or higher
- A modern web browser (Chrome, Firefox, Safari, etc.)

# How to run
- Clone the repository: git clone https://github.com/anandgpatel/AMaze.git
- Navigate to project directory: cd AMaze
- Run the application: python main.py or python3 main.py
- Select algorithm from the menu
- The solved maze will automatically open in your default web browser

# Maze format
```text
A = Start
Z = Goal
# = Wall
Space = Open path

You can edit the maze using format above.
```
# Maze (15x15)
```text
###############
#A   #      # #
# ### ##### # #
#   #     #   #
### # ### # ###
#   # #   #   #
# ### # ### ###
#     #   #   #
##### ### ### #
#   #   #     #
# # ### # ### #
# #     # Z # #
# ##### ### # #
#       #     #
###############
```
# Technology used
- Python
- Data structure (Stack, Queue, Priority Queue)
- Heuristic search
- HTML/CSS

# Author
Anand Patel
