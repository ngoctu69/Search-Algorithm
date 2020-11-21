### AI - Search
**DESCRIPTION HOW SEARCH ALGORITHMS WORK**

We have 4 search algorithms in this lab: BFS, DFS, UCS, A_Star. These algorithms are programmed in file **search_algorithm.py**.

Input:
- **graph**: list of graph. Example: graph = [[(139, 140), [1, 2], (100, 100, 100), (0, 0, 0)], [(312, 224), [0, 2, 3, 4], (100, 100, 100), (0, 0, 0)],...]. In this example, graph[0] is vertex 0, graph[1] is vertex 1.
	+ (139,140): position of vertex when drawing on screen
	+ [1,2]: list of adjacent vertices
	+ (100,100,100): border color of vertex 
	+ (0,0,0): color of vertex 
- **edges**: list of graph's edges. Example: edges[edge_id(0,1)] = [(0,1), (0,0,0)]. The edge from vertex 0 to vertex 1 with color (0,0,0) (black)
- **edge_id**: id of edge
- **start**: starting vertex
- **goal**: goal vertex
- **input.txt**: line 1 is starting vertex, line 2 is goal vertex, others are edges of graph
- colors in **node_color.py**:
	+ blue: passed vertex
	+ red: browsing vertex
	+ black: unbrowsed vertex
	+ yellow: current vertex
	+ purple: goal vertex
	+ orange: starting vertex
	+ green: edges of result 
	+ gray: unbrowsed edge
	+ white: browsed edge <br />
- In order to update new status, use: **graphUI.updateUI()**.

**Note**: read code function **example_func()** in file **search_algorithm.py** to understand how to set color for vertices, edges.


**To run project**
1. Create virtual environment (if necessary)

	`virtualenv venv`
	`source venv/bin/activate`
2. Install package

	`pip install -r requirement.txt`
3. Run code

Argument from command line. To run: 

`python main.py input_file search_algorithm`

*search_algorithm* must be one of ['bfs', 'dfs', 'ucs', 'a_star',...]

For example:
	`python main.py input.txt bfs`

**Note**: to run sample code: `python main.py input.txt`
