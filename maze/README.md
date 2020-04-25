### DFS

[https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

Search until the max depth of a given graph/tree.

A ongoing uses two data structures: a Stack of states  to track the places we can search "frontier", and a set of states we have already searched "explored". We need "explored" list to avoid search again at places we have already searched.
While there are still places to search at the "frontier" we keep testing if this place is the Goal.
When the "frontier" stack if empty, it means that we don't need to searck anymore.

In this implementation we are using a "Node" to keep track of how our state has changed (from one position to another).
Given the context of our Maze, the Node tracks MazeLocations.
