class Board:
    def __init__(self, moles):
        self.board = [] * 6
        for i in range(0, 6):
            self.board.append([0] * 6)
        for mole in moles:
            column = (mole - 1) % 4
            row = (mole - 1) // 4
            self.board[row + 1][column + 1] = 1

    def print(self):
        for row in range(4, 0, -1):
            for column in range(1,5):
                print(self.board[row][column], end="", flush=True)
            print()

    def whack(self, mole):
        column = (mole - 1) % 4
        row = (mole - 1) // 4
        # Center
        self.board[row + 1][column + 1] = (self.board[row + 1][column + 1] + 1) % 2
        # Top and bottom
        for i in range(-1, 2):
            self.board[row + 1 + i][column + 1] = (self.board[row + 1 + i][column + 1] + 1) % 2
        # Sides
        for i in range(-1, 2):
            self.board[row + 1][column + 1 + i] = (self.board[row + 1][column + 1 + i] + 1) % 2

    def check(self):
        for row in range(1, 5):
            for column in range(1, 5):
                if self.board[row][column] == 1:
                    return False
        return True

    def is_there_mole(self, position):
        column = ((position - 1) % 4) + 1
        row = ((position - 1) // 4) + 1
        if self.board[row][column] == 1:
            return True
        return False


def dfs_search(board, limiter):
    if limiter == 0:
        return False, []
    for hole in range(1, 17):
        if board.is_there_mole(hole):
            board.whack(hole)
            if board.check():
                return True, [hole]
            state, solution = dfs_search(board, limiter - 1)
            if state == True:
                solution = [hole] + solution
                return state, solution
            board.whack(hole)
    return False, []


def bfs_search(board, limiter, visited=[]):

    if limiter == 0:
        return False, []

    for hole in range(1, 17):
        # check for mole
        if board.is_there_mole(hole):

            # checking is hole already visited
            if hole not in visited:
                visited.append(hole)
                board.whack(hole)

                # checking if board is clear
                if board.check():
                    return True, [hole]

                # un-whacking hole to get to original board
                board.whack(hole)

                # if all the holes are visited then move to the next layer

                # calling up recursively
                state, solution = bfs_search(board, limiter - 1)
                if state == True:
                    solution = [hole] + solution
                    return state, solution


        return False, []



#state, solution = dfs_search(board, 5)
#print(solution)

moles= [5,1,3,9]
board = Board(moles)

state, solution = dfs_search(board, 5)

print(solution)
board = Board(moles)
board.print()
for whack in solution:
    print()
    board.whack(whack)
    board.print()
