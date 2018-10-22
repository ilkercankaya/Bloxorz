import numpy as np
from queue import PriorityQueue
import Bloxorz
import math
import time
start_time = time.time()
import tracemalloc
tracemalloc.start()

def h_n(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def g_n(prevcost):
    prevcost = prevcost + 1
    return prevcost


# f(n) = g(n) + h(n) Heuristic Function
def f_n(frontier, goal):
    # Check if the box is perpendicular or not
    if frontier[1][1][1] != []:
        # Take average of the points and calculate distance
        return g_n(frontier[0]) + h_n((frontier[1][1][0][0] + frontier[1][1][1][0]) / 2,
                                      (frontier[1][1][0][1] + frontier[1][1][1][1]) / 2, goal[0], goal[1])
    else:
        return g_n(frontier[0]) + h_n(frontier[1][1][0][0], frontier[1][1][0][1], goal[0], goal[1])


def successorfunction(block, q, next_frontier, visitedNodes):
    # If movable then ca1culate post and put it in the queue and update the nodes
    # Handle each first move and node list differently
    if block.ismovableup():
        # If its not the inital node
        if next_frontier != False:
            # If Not visited before
            if block.getup() not in visitedNodes:
                q.put((f_n(next_frontier, block.board.goal), [next_frontier[1][0] + ['Up'], block.getup()]))
        else:
            q.put((1, [['Up'], block.getup()]))
    if block.ismovableright():
        # If its not the inital node
        if next_frontier != False:
            # If Not visited before
            if block.getright() not in visitedNodes:
                q.put((f_n(next_frontier, block.board.goal), [next_frontier[1][0] + ['Right'], block.getright()]))
        else:
            q.put((1, [['Right'], block.getright()]))
    if block.ismovabledown():
        # If its not the inital node
        if next_frontier != False:
            # If Not visited before
            if block.getdown() not in visitedNodes:
                q.put((f_n(next_frontier, block.board.goal), [next_frontier[1][0] + ['Down'], block.getdown()]))
        else:
            q.put((1, [['Down'], block.getdown()]))
    if block.ismovableleft():
        # If its not the inital node
        if next_frontier != False:
            # If Not visited before
            if block.getleft() not in visitedNodes:
                q.put((f_n(next_frontier, block.board.goal), [next_frontier[1][0] + ['Left'], block.getleft()]))
        else:
            q.put((1, [['Left'], block.getleft()]))


#   Config the Board, the player is put manually on the constructor of the player

boardstructure = [['O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'G', 'X'],
                  ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O'],
                  ['X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X']]

# boardstructure = [['G', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#                   ['O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X'],
#                   ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
#                   ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#                   ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O'],
#                   ['X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X']]
#
# boardstructure = [['O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#                   ['O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X'],
#                   ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
#                   ['X', 'G', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
#                   ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O'],
#                   ['X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X']]

board = Bloxorz.Board(np.array(boardstructure))

# Config the block on the board
mode = 1
config = 1
gameblock = Bloxorz.Block(board, mode, config, [2, 3], [3, 3])
gameblock.printfield()

pQ = PriorityQueue()
path = []
visited = []

while not gameblock.isgamewon():
    # Get the next path if exists
    # See if the element is taken from qeueue
    nq = False
    if not pQ.empty():
        next_frontier_q = pQ.get()
        print("Popped", next_frontier_q)
        nq = next_frontier_q
        # Append Visited List
        visited.append([next_frontier_q[1][1][0], next_frontier_q[1][1][1], next_frontier_q[1][1][2],
                        next_frontier_q[1][1][3]])
        # Re-initiliaze Board With Block
        board = Bloxorz.Board(np.array(boardstructure))
        path = next_frontier_q[1][0]
        # Respawn the block in the box
        gameblock = Bloxorz.Block(board, next_frontier_q[1][1][2], next_frontier_q[1][1][3], next_frontier_q[1][1][0],
                                  next_frontier_q[1][1][1])
        gameblock.printfield()

    # Calculate Successors
    successorfunction(gameblock, pQ, nq, visited)
print("\n Solution Found!", path)
print("--- %s Time Taken ---" % (time.time() - start_time))
# Get the peak memory used
print("Peak Memory Used", tracemalloc.get_traced_memory()[1])

