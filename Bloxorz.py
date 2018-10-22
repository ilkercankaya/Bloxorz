# 0 is for perpendicular mode
# 1 is for flat mode
# 0 is for X-Axis config
# 1 is for Y-Axis mode
from copy import deepcopy

class Block:
    def __init__(self, givenboard, mode, config, positionfirstbox, positionsecondbox):
        # Copy Board
        self.board = givenboard
        # Fill the Board with Block
        self.board.field[positionfirstbox[0]][positionfirstbox[1]] = 2
        if positionsecondbox != []:
            self.board.field[positionsecondbox[0]][positionsecondbox[1]] = 2
        self.mode = mode
        self.config = config
        self.positionFirstBox = positionfirstbox
        self.positionSecondBox = positionsecondbox

    def isgamewon(self):
        if self.mode == 0 and self.positionFirstBox == self.board.goal:
            return True
        else:
            return False

    def ismovableleft(self):
        try:
            if self.mode == 0:
                if self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] - 1] != 1 \
                        and self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] - 2] != 1:
                    return True
                else:
                    return False
            elif self.mode == 1:
                if self.config == 0:
                    if self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] - 1] != 1:
                        return True
                    else:
                        return False
                if self.config == 1:
                    if self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] - 1] != 1 \
                            and self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1] - 1] != 1:
                        return True
                    else:
                        return False
        except IndexError:
            return False

    def ismovableright(self):
        try:
            if self.mode == 0:
                if self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] + 1] != 1 \
                        and self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] + 2] != 1:
                    return True
                else:
                    return False
            elif self.mode == 1:
                if self.config == 0:
                    if self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1] + 1] != 1:
                        return True
                    else:
                        return False
                if self.config == 1:
                    if self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] + 1] != 1 \
                            and self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1] + 1] != 1:
                        return True
                    else:
                        return False
        except IndexError:
            return False

    def ismovableup(self):
        try:
            if self.mode == 0:
                if self.board.field[self.positionFirstBox[0] - 1][self.positionFirstBox[1]] != 1 \
                        and self.board.field[self.positionFirstBox[0] - 2][self.positionFirstBox[1]] != 1:
                    return True
                else:
                    return False
            elif self.mode == 1:
                if self.config == 0:
                    if self.board.field[self.positionFirstBox[0] - 1][self.positionFirstBox[1]] != 1 \
                            and self.board.field[self.positionSecondBox[0] - 1][self.positionSecondBox[1]] != 1:
                        return True
                    else:
                        return False
                elif self.config == 1:
                    if self.board.field[self.positionFirstBox[0] - 1][self.positionFirstBox[1]] != 1:
                        return True
                    else:
                        return False
        except IndexError:
            return False

    def ismovabledown(self):
        try:
            if self.mode == 0:
                if self.board.field[self.positionFirstBox[0] + 1][self.positionFirstBox[1]] != 1 \
                        and self.board.field[self.positionFirstBox[0] + 2][self.positionFirstBox[1]] != 1:
                    return True
                else:
                    return False
            elif self.mode == 1:
                if self.config == 0:
                    if self.board.field[self.positionFirstBox[0] + 1][self.positionFirstBox[1]] != 1 \
                            and self.board.field[self.positionSecondBox[0] + 1][self.positionSecondBox[1]] != 1:
                        return True
                    else:
                        return False
                elif self.config == 1:
                    if self.board.field[self.positionSecondBox[0] + 1][self.positionSecondBox[1]] != 1:
                        return True
                    else:
                        return False
        except IndexError:
            return False

    def getleft(self):
        if self.mode == 0:
            # Object location
            secondbox = [self.positionFirstBox[0], self.positionFirstBox[1] - 1]
            firstbox = [self.positionFirstBox[0], self.positionFirstBox[1] - 2]
            return [firstbox, secondbox, 1, 0]

        elif self.mode == 1:
            if self.config == 0:
                firstbox = [self.positionFirstBox[0], self.positionFirstBox[1] - 1]
                return [firstbox, [], 0, self.config]
            if self.config == 1:
                positionSecondBox = [self.positionSecondBox[0], self.positionSecondBox[1] - 1]
                positionFirstBox = [self.positionFirstBox[0], self.positionFirstBox[1] - 1]
                return [positionFirstBox, positionSecondBox, 1, self.config]

    def moveleft(self):
        if self.mode == 0:
            if self.ismovableleft():
                # Erase the object from board
                self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                # Re-put object
                self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] - 1] = 2
                self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] - 2] = 2
                # Update object location
                self.positionSecondBox = [self.positionFirstBox[0], self.positionFirstBox[1] - 1]
                self.positionFirstBox = [self.positionFirstBox[0], self.positionFirstBox[1] - 2]
                # Change Mode and Config
                self.mode = 1
                self.config = 0
                return True
            else:
                return False

        elif self.mode == 1:
            if self.ismovableleft():
                if self.config == 0:
                    # Erase the object from board
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1]] = 0
                    # Re-put object
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] - 1] = 2
                    # Update object location
                    self.positionSecondBox = []
                    self.positionFirstBox = [self.positionFirstBox[0], self.positionFirstBox[1] - 1]
                    # Change Mode
                    self.mode = 0
                    return True
                if self.config == 1:
                    # Erase the object from board
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1]] = 0
                    # Re-put object
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] - 1] = 2
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1] - 1] = 2
                    # Update object location
                    self.positionSecondBox = [self.positionSecondBox[0], self.positionSecondBox[1] - 1]
                    self.positionFirstBox = [self.positionFirstBox[0], self.positionFirstBox[1] - 1]
                    return True
            else:
                return False

    def moveright(self):
        if self.mode == 0:
            if self.ismovableright():
                # Erase the object from board
                self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                # Re-put object
                self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] + 1] = 2
                self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] + 2] = 2
                # Update object location
                self.positionSecondBox = [self.positionFirstBox[0], self.positionFirstBox[1] + 2]
                self.positionFirstBox = [self.positionFirstBox[0], self.positionFirstBox[1] + 1]
                # Change Mode
                self.mode = 1
                self.config = 0
                return True
            else:
                return False

        elif self.mode == 1:
            if self.ismovableright():
                if self.config == 0:
                    # Erase the object from board
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1]] = 0
                    # Re-put object
                    self.board.field[self.positionFirstBox[0]][self.positionSecondBox[1] + 1] = 2
                    # Update object location
                    self.positionFirstBox = [self.positionFirstBox[0], self.positionSecondBox[1] + 1]
                    self.positionSecondBox = []
                    # Change Mode
                    self.mode = 0
                    return True
                if self.config == 1:
                    # Erase the object from board
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1]] = 0
                    # Re-put object
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1] + 1] = 2
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1] + 1] = 2
                    # Update object location
                    self.positionFirstBox = [self.positionFirstBox[0], self.positionFirstBox[1] + 1]
                    self.positionSecondBox = [self.positionSecondBox[0], self.positionSecondBox[1] + 1]
                    return True
            else:
                return False

    def getright(self):
        if self.mode == 0:
            # Object location
            secondbox = [self.positionFirstBox[0], self.positionFirstBox[1] + 2]
            firstbox = [self.positionFirstBox[0], self.positionFirstBox[1] + 1]
            return [firstbox, secondbox, 1, 0]

        elif self.mode == 1:
            if self.config == 0:
                firstbox = [self.positionFirstBox[0], self.positionSecondBox[1] + 1]
                return [firstbox, [], 0, self.config]
            if self.config == 1:
                positionFirstBox = [self.positionFirstBox[0], self.positionFirstBox[1] + 1]
                positionSecondBox = [self.positionSecondBox[0], self.positionSecondBox[1] + 1]
                return [positionFirstBox, positionSecondBox, self.mode, self.config]

    def moveup(self):
        if self.mode == 0:
            if self.ismovableup():
                # Erase the object from board
                self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                # Re-put object
                self.board.field[self.positionFirstBox[0] - 1][self.positionFirstBox[1]] = 2
                self.board.field[self.positionFirstBox[0] - 2][self.positionFirstBox[1]] = 2
                # Update object location
                self.positionSecondBox = [self.positionFirstBox[0] - 1, self.positionFirstBox[1]]
                self.positionFirstBox = [self.positionFirstBox[0] - 2, self.positionFirstBox[1]]
                # Change Mode
                self.mode = 1
                self.config = 1
                return True
            else:
                return False
        elif self.mode == 1:
            if self.ismovableup():
                if self.config == 0:
                    # Erase the object from board
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1]] = 0
                    # Re-put object
                    self.board.field[self.positionFirstBox[0] - 1][self.positionFirstBox[1]] = 2
                    self.board.field[self.positionSecondBox[0] - 1][self.positionSecondBox[1]] = 2
                    # Update object location
                    self.positionSecondBox = [self.positionSecondBox[0] - 1, self.positionSecondBox[1]]
                    self.positionFirstBox = [self.positionFirstBox[0] - 1, self.positionFirstBox[1]]
                    return True
                elif self.config == 1:
                    # Erase the object from board
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1]] = 0
                    # Re-put object
                    self.board.field[self.positionFirstBox[0] - 1][self.positionFirstBox[1]] = 2
                    # Update object location
                    self.positionFirstBox = [self.positionFirstBox[0] - 1, self.positionFirstBox[1]]
                    self.positionSecondBox = []
                    # Change Mode
                    self.mode = 0
                    return True
            else:
                return False

    def getup(self):
        if self.mode == 0:
            # Object location
            secondbox = [self.positionFirstBox[0] - 1, self.positionFirstBox[1]]
            firstbox = [self.positionFirstBox[0] - 2, self.positionFirstBox[1]]
            return [firstbox, secondbox, 1, 1]

        elif self.mode == 1:
            if self.config == 0:
                positionSecondBox = [self.positionSecondBox[0] - 1, self.positionSecondBox[1]]
                positionFirstBox = [self.positionFirstBox[0] - 1, self.positionFirstBox[1]]
                return [positionFirstBox, positionSecondBox, self.mode, self.config]
            if self.config == 1:
                positionFirstBox = [self.positionFirstBox[0] - 1, self.positionFirstBox[1]]
                positionSecondBox = []
                return [positionFirstBox, positionSecondBox, 0, self.config]

    def movedown(self):
        if self.mode == 0:
            if self.ismovabledown():
                # Erase the object from board
                self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                # Re-put object
                self.board.field[self.positionFirstBox[0] + 1][self.positionFirstBox[1]] = 2
                self.board.field[self.positionFirstBox[0] + 2][self.positionFirstBox[1]] = 2
                # Update object location
                self.positionSecondBox = [self.positionFirstBox[0] + 2, self.positionFirstBox[1]]
                self.positionFirstBox = [self.positionFirstBox[0] + 1, self.positionFirstBox[1]]
                # Change Mode
                self.mode = 1
                self.config = 1
                return True
            else:
                return False
        elif self.mode == 1:
            if self.ismovabledown():
                if self.config == 0:
                    # Erase the object from board
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1]] = 0
                    # Re-put object
                    self.board.field[self.positionFirstBox[0] + 1][self.positionFirstBox[1]] = 2
                    self.board.field[self.positionSecondBox[0] + 1][self.positionSecondBox[1]] = 2
                    # Update object location
                    self.positionSecondBox = [self.positionSecondBox[0] + 1, self.positionSecondBox[1]]
                    self.positionFirstBox = [self.positionFirstBox[0] + 1, self.positionFirstBox[1]]
                    return True
                elif self.config == 1:
                    # Erase the object from board
                    self.board.field[self.positionFirstBox[0]][self.positionFirstBox[1]] = 0
                    self.board.field[self.positionSecondBox[0]][self.positionSecondBox[1]] = 0
                    # Re-put object
                    self.board.field[self.positionSecondBox[0] + 1][self.positionSecondBox[1]] = 2
                    # Update object location
                    self.positionFirstBox = [self.positionSecondBox[0] + 1, self.positionFirstBox[1]]
                    self.positionSecondBox = []
                    # Change Mode
                    self.mode = 0
                    return True
            else:
                return False

    def getdown(self):
        if self.mode == 0:
            # Object location
            secondbox = [self.positionFirstBox[0] + 2, self.positionFirstBox[1]]
            firstbox = [self.positionFirstBox[0] + 1, self.positionFirstBox[1]]
            return [firstbox, secondbox, 1, 1]

        elif self.mode == 1:
            if self.config == 0:
                # Adjust the box positions
                positionSecondBox = [self.positionSecondBox[0] + 1, self.positionSecondBox[1]]
                positionFirstBox = [self.positionFirstBox[0] + 1, self.positionFirstBox[1]]
                return [positionFirstBox, positionSecondBox, self.mode, self.config]
            if self.config == 1:
                # Adjust the box positions
                positionFirstBox = [self.positionSecondBox[0] + 1, self.positionFirstBox[1]]
                positionSecondBox = []
                return [positionFirstBox, positionSecondBox, 0, self.config]

    def printfield(self):
        printer = deepcopy(self.board.field).astype(str)
        # Transfer the field and print
        for i in range(self.board.field.shape[0]):
            for j in range(self.board.field.shape[1]):
                if self.board.field[i][j] == 1:
                    printer[i][j] = 'X'
                elif self.board.field[i][j] == 0:
                    printer[i][j] = 'O'
                elif self.board.field[i][j] == 2:
                    printer[i][j] = 'S'
                elif self.board.field[i][j] == 3:
                    printer[i][j] = 'G'
        print("Current Board: \n", printer,"\n")


class Board:
    def __init__(self, array):
        # Conver the board and store
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                if array[i][j] == 'X':
                    array[i][j] = 1
                elif array[i][j] == 'O':
                    array[i][j] = 0
                elif array[i][j] == 'S':
                    array[i][j] = 2
                elif array[i][j] == 'G':
                    array[i][j] = 3

        self.field = array.astype(int)
        for i in range(self.field.shape[0]):
            for j in range(self.field.shape[1]):
                if self.field[i][j] == 3:
                    # Update Field And Set The Goal Point
                    self.field[i][j] = 0
                    self.goal = [i, j]
                    break
