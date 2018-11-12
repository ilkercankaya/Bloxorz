# Bloxorz
Bloxorz is a game where the goal is to drop a 1 × 2 × 1 block through a hole in the
middle of a board without falling off its edges.

![Boloxorz](http://jpg.hoodamath.com/large/bloxorz_300x225.jpg)
## Goal

_Using A* Search and Uniform Cost Search to solve a stage with a goal given on a board._

Input of the problem The input game board of size m×n is represented by a matrix
of size m × n where:  

• O denotes safe tiles: the block can stand on these anytime;  
• X denotes empty tiles: the block may never touch an empty tile, even if half of
the block is on a safe tile;  
• S denotes the tile(s) occupied by the block: if the block is in the vertical orientation
then there is one tile labeled S, otherwise (if the block is in the horizontal
orientation) there are two adjacent tiles labeled S;  
• G denotes the goal tile: the block needs to be on it (vertically) in order to fall
into the goal.  

For instance, the matrix below represents the game board depicted below 

**O O O X X X X X X X  
O O O O O O X X X X  
O O O S O O O O O X  
X O O S O O O O O O  
X X X X X O O G O O  
X X X X X X O O O X**  

## The Files

`Bloxorz.py:` Contains an implementation of Bloxorz from scratch.

`play.py:` You can play the game in 2D from the console by running this file.

`AStarSearch.py:` Solves the game with a given board and a goal by using A*Search. Also prints the optimal solution, time taken to find the solution, peak memory consumption during the process

`UcsSearch.py:` Solves the game with a given board and a goal by using UCS. Also prints the optimal solution, time taken to find the solution, peak memory consumption during the process

## Algorithms used to solve the problem

- A* Search
- Uniform Cost Search

## Example folutions found by the algorithm

`['Right', 'Right', 'Right', 'Down', 'Down', 'Right']`

`['Right', 'Down', 'Right', 'Right', 'Down', 'Right']`

## More Information with A Report
[Report](report.pdf)
