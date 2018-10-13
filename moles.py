class Node:
    def __init__(self):
        self.rootNode = None
        self.children = []

    def add_child(self, grid):
        self.children.append(grid)



def board(moles):

    node = Node()
    # 5 x 5 grid for spill overs

    holes = [] * 5
    for i in range(0, 5):
        holes.append([0] * 5)

    for x in moles:
        row = int(x/5)

        column = x - row * 4

        holes[row+1][column] = 1

    if node.rootNode is None:

        node.rootNode = holes

    return search(holes)

def check(grid):

    for i in range(1,5):
        for x in range(1, 5):
            if grid[i][x] == 0:
                pass
            else:
                return True, i, x
    return False

def search(board , limit = 15):

    if limit == 0:
        return False

    for hole in range(0, 15):

        # whack mole
        true, row, column = check(board)
        board[row][column] = (board[row][column] - 1) * -1
        for i in range(-1, 2):
            board[row + i][column] = (board[row + i][column] - 1) * -1

        for i in range(-1, 2):
            board[row][column + i] = (board[row][column + i] - 1) * -1

        # check if the board is clear
        print(board)

        if check(board) is False:
            board.append(hole)

        state, solution = search(board, limit -1)

        if state is True:
            return True, [solution, hole]
        return False


print(board([1,4,5,6]))
