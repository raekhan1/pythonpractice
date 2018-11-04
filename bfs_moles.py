class Board:
    def __init__(self, moles):
        self.board = [] * 6
        for i in range(0,6):
            self.board.append([0] * 6)
        for mole in moles:
            column = (mole - 1) % 4
            row = (mole - 1) // 4
            self.board[row + 1][column + 1] = 1

    def print(self):
        for row in range(4,0,-1):
            for column in range(1,5):
                print(self.board[row][column], end="", flush=True)
            print()

    def return_board(self):
        return self.board

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
        for row in range(1,5):
            for column in range(1,5):
                if self.board[row][column] == 1:
                    return False
        return True

    def is_there_mole(self, position):
        column = ((position - 1) % 4) + 1
        row = ((position - 1) // 4 ) + 1
        if self.board[row][column] == 1:
            return True
        return False


def search(board, limiter):
    if limiter == 0:
        return False, []
    for hole in range(1, 17):
        if board.is_there_mole(hole):
            board.whack(hole)
            if board.check():
                return True, [hole]
            state, solution = search(board, limiter - 1)
            if state is True:
                solution = [hole] + solution
                return state, solution
            board.whack(hole)
    return False, []


def bfs_search(board):

    # used to break out of the while loop
    last_mole = None

    # start node
    queue = [board]

    while len(queue) != 0:

        temp = queue[0]
        # saving current board
        del queue[0]
        # deleting board from the queue

        moles = []
        # finding moles on the board
        for hole in range(0, 17):
            if temp.is_there_mole(hole):
                moles.append(hole)

        # finding children of the board
        for mole in moles:

            current_board = Board(moles)

            print('')
            current_board.print()

            current_board.whack(mole)
            queue.append(current_board)
            if current_board.check():

                print('')
                current_board.print()

                last_mole = mole
                break

            print('')
            current_board.print()

        if last_mole is not None:
            break

    path_queue = [[last_mole]]
    visited = []
    start_mole = []
    b = Board([])

    for hole in range(0, 17):
        if board.is_there_mole(hole):
            start_mole = start_mole + [hole]
    print(start_mole)

    while path_queue != 0:
        moles = []

        b.print()
        for i in path_queue[-1]:
            b.whack(i)

        path = path_queue[0]
        print(path_queue)

        if path == start_mole:
            return path

        elif path not in visited:

            for mole in range(0, 17):
                if b.is_there_mole(mole):
                   moles.append(mole)

            new_path = path + moles
            path_queue.append(new_path)
            visited.append(new_path)




moles = [1,2,4,8,9,10,11,14]
#moles = [3,4,8]
board = Board(moles)
print(bfs_search(board))

# state, solution = search(board, 5)
# print(solution)
#
# board = Board(moles)
# board.print()
# for whack in solution:
#     print()
#     board.whack(whack)
#     board.print()
