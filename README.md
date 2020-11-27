# Path Finder

![](/path-finder.png)

## Algorithms

**For Maze Generation**

[Randomized DFS](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Iterative_implementation)

The general idea is to randomly choose a neighbour of the current node and visit it, also we break the wall between the current node and the neighbour node. 

This algorithm creates perfect maze or a maze that has no loops, so for every two points in the maze there is only one solution.

So, to get some loops in the maze I am implemented this algorithm in a slightly different way. In the above algorithm all node are visited only once but now some node in the maze could be re visited ( there is a 60% probability that a node could be re visited ). Now, all the nodes could be visited at max twice.

**For Path Finding**

[A Star](https://en.wikipedia.org/wiki/A*_search_algorithm)


## Dependencies

[Tkinter](https://tkdocs.com/tutorial/index.html)
