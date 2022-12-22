# https://adventofcode.com/2022/day/22
from dataclasses import dataclass
import re

board = []
drawboard = []
ARROWS = {0: ">", 1: "v", 2: "<", 3: "^"}
isPart2 = False


@dataclass
class Me:
    x: int
    y: int
    direction: int  # 0=R 1=D 2=L 3=U

    # def wrap3DTest(self):  # return tuple with new pos and direction
    #     match self.direction:
    #         case 0:  # right
    #             if self.y < 4:
    #                 return 15, 11 - self.y, 2
    #             elif self.y < 8:
    #                 return 15 - self.y + 4, 8, 1
    #             else:
    #                 return 11, 4 - self.y + 8, 2
    #         case 1:  # down
    #             if self.x < 4:
    #                 return 11 - self.x, 11, 3
    #             elif self.x < 8:
    #                 return 8, 11 - self.x + 4, 0
    #             elif self.x < 12:
    #                 return 4 - self.x + 8, 7, 3
    #             else:
    #                 return 0, 7 - self.x + 12, 0
    #         case 2:
    #             pass  # too lazy to do it
    #         case 3:
    #             pass  # too lazy to do it

    def wrap2D(self):
        match self.direction:
            case 0:  # right
                return next(x for x in range(len(board[self.y])) if board[self.y][x] != " "), self.y, 0
            case 1:  # down
                return self.x, next(y for y in range(len(board)) if board[y][self.x] != " "), 1
            case 2:  # left
                return len(board[self.y]) - 1, self.y, 2
            case 3:  # up
                return self.x, next(y for y in range(len(board) - 1, -1, -1) if findInBoard(self.x, y) != " "), 3

    def wrap3D(self):
        """returns tuple with new position x, y and direction"""
        match self.direction:
            case 0:  # right
                if self.y < 50:  # right of 2 -> right of 5 reversed
                    return 99, 149 - self.y, 2
                elif self.y < 100:  # right of 3 -> down of 2
                    return self.y + 50, 49, 3
                elif self.y < 150:  # right of 5 -> right of 2 reversed
                    return 149, 49 - self.y + 100, 2
                else:  # right of 6 -> down of 5
                    return self.y - 100, 149, 3
            case 1:  # down
                if self.x < 50:  # down of 6 -> up of 2
                    return self.x + 100, 0, 1
                elif self.x < 100:  # down of 5 -> right of 6
                    return 49, self.x + 100, 2
                else:  # down of 2 -> right of 3
                    return 99, self.x - 50, 2
            case 2:  # left
                if self.y < 50:  # left of 1 -> left of 4 reverse
                    return 0, 149 - self.y, 0
                elif self.y < 100:  # left of 3 -> up of 4
                    return self.y - 50, 100, 1
                elif self.y < 150:  # left of 4 -> left of 1 reverse
                    return 50, 49 - self.y + 100, 0
                else:  # left of 6 -> up of 1
                    return self.y - 100, 0, 1
            case 3:  # up
                if self.x < 50:  # up of 4 -> left of 3
                    return 50, self.x + 50, 0
                elif self.x < 100:  # up of 1 -> left of 6
                    return 0, self.x + 100, 0
                else:  # up of 2 -> down of 6
                    return self.x - 100, 199, 3

    def moveWrap(self):
        x, y, dir = self.wrap3D() if isPart2 else self.wrap2D()
        if findInBoard(x, y) == ".":
            self.x = x
            self.y = y
            self.direction = dir

    def drawPosition(self):
        s = drawboard[self.y]
        drawboard[self.y] = s[: self.x] + ARROWS[self.direction] + s[self.x + 1 :]

    def moveBy1(self, offsetX, offsetY):
        match findInBoard(self.x + offsetX, self.y + offsetY):
            case ".":
                self.x += offsetX
                self.y += offsetY
            case " ":
                self.moveWrap()
            case "#":
                pass

    def move(self, size: int):
        for i in range(size):
            match self.direction:
                case 0:  # right
                    self.moveBy1(1, 0)
                case 1:  # down
                    self.moveBy1(0, 1)
                case 2:  # left
                    self.moveBy1(-1, 0)
                case 3:  # up
                    self.moveBy1(0, -1)
            self.drawPosition()


def findInBoard(x, y):
    if x == -1 or y == -1 or y >= len(board) or x >= len(board[y]):
        return " "
    return board[y][x]


with open("2022/input_files/day22") as f:
    data = "".join([line for line in f])
    groups = [group.split("\n") for group in data.split("\n\n")]

board = groups[0]
drawboard = board.copy()
instructions = groups[1][0]

moveSizes = list(map(int, re.findall(r"(\d+)", instructions)))
turns = re.findall(r"([A-Z]+)", instructions)

me = Me(board[0].index("."), 0, 0)

for moveSize, turn in zip(moveSizes, turns):
    me.move(moveSize)
    me.direction += 1 if turn == "R" else -1
    me.direction %= 4
me.move(moveSizes[-1])

password = 1000 * (me.y + 1) + 4 * (me.x + 1) + me.direction
print(f"{me=}")
print(f"{password=}")
