import webbrowser
import os

#Solved maze
def solvedMaze(maze, visitedStates, path, algorithm, cost, filename="solved.html"):
    htmlStart = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Solved maze</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: 'Roboto', sans-serif;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    margin: 0;
                    padding: 20px;
                    background-color: #f0f2f5;
                }}

                .info {{
                    text-align: center;
                    margin-bottom: 20px;
                    font-size: 18px;
                    color: #555;
                }}

                .grid {{
                    display: grid;
                    grid-template-columns: repeat({len(maze[0])}, minmax(15px, 2.5vw));
                    grid-auto-rows: minmax(15px, 2.5vw);
                    gap: 2px;
                }}

                .cell {{
                    border-radius: 5px;
                    border: 1px solid #555;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-weight: bold;
                    color: white;
                    font-size: 0.8rem;
                    line-height = 1;
                    transition: all 0.3s ease;
                }}

                .wall {{
                    background-color: #8B4513;
                }}

                .visitedStates {{
                    background-color: #A9A9A9;
                }}

                .path {{
                    background-color: #4CAF50;
                }}

                .start {{
                    background-color: #2196F3;
                }}

                .goal {{
                    background-color: #FF9800;
                }}

                .empty {{
                    background-color: #E0E0E0;
                    color: #555;
                }}
            </style>
        </head>
        <body>
            <div class="info">
                Algorithm: {algorithm} <br>
                Path cost: {cost} <br>
                Total visited nodes: {len(visitedStates)}
            </div>
            <div class="grid">
    """

    htmlCells = ""
    pathSet = set(path)

    for row in range(len(maze)):
        for column in range(len(maze[0])):
            cell = maze[row][column]
            classes = "cell"

            if (row, column) in pathSet:
                if cell == "A":
                    classes += " start"
                    display = "Start"
                elif cell == "Z":
                    classes += " goal"
                    display = "End"
                else:
                    classes += " path"
                    display = ""
            elif (row, column) in visitedStates:
                classes += " visitedStates"
                display = ""
            else:
                if cell == "#":
                    classes += " wall"
                else:
                    classes += " empty"
                display = ""

            htmlCells += f'<div class="{classes}">{display}</div>\n'

    htmlEnd = """
            </div>
        </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(htmlStart + htmlCells + htmlEnd)

    filePath = os.path.abspath("solved.html")
    webbrowser.open(f"file://{filePath}")