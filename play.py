import numpy as np
import Bloxorz

boardstructure = [['O', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'X'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'G', 'X'],
                  ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O'],
                  ['X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X']]

board = Bloxorz.Board(np.array(boardstructure))

# Config the block on the board
mode = 1
config = 1
gameblock = Bloxorz.Block(board, mode, config, [2, 3], [3, 3])
gameblock.printfield()

from tkinter import *

main = Tk()


def leftKey(event):
    print("Left")
    if not gameblock.moveleft():
        main.quit()
        print("You DIED!")
    gameblock.printfield()
    if gameblock.isgamewon():
        print("You have won!")
        main.quit()
    print("\n")


def rightKey(event):
    print("Right")
    if not gameblock.moveright():
        main.quit()
        print("You DIED!")
    gameblock.printfield()
    if gameblock.isgamewon():
        print("You have won!")
        main.quit()
    print("\n")


def upKey(event):
    print("Up")
    if not gameblock.moveup():
        main.quit()
        print("You DIED!")
    gameblock.printfield()
    if gameblock.isgamewon():
        print("You have won!")
        main.quit()
    print("\n")


def downKey(event):
    print("Down")
    if not gameblock.movedown():
        main.quit()
        print("You DIED!")
    gameblock.printfield()
    if gameblock.isgamewon():
        print("You have won!")
        main.quit()
    print("\n")

# Assign keys action
frame = Frame(main, width=100, height=100)
main.bind('<Left>', leftKey)
main.bind('<Up>', upKey)
main.bind('<Down>', downKey)

main.bind('<Right>', rightKey)
frame.pack()
main.mainloop()
