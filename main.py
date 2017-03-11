import numpy as np

def generateBoard(size):
    side_size = np.power(size, 2)
    board = np.zeros(shape=(side_size, side_size))
    board = fillBoard(board, size, side_size)


def fillBoard(board, size, side_size):
    # fill the sectors in the diagonal (no conflict possible)
    # sectors stores the values of the sectors of the board
    sectors = []
    for iter in range(side_size):
        sectors.append([])

    for block_index in range(size):
        block = np.random.permutation(np.arange(1, side_size + 1)).reshape(size, size)
        for block_row in range(size):
            for block_col in range(size):
                row = block_row + block_index * size
                col = block_col + block_index * size
                board[col][row] = block[block_col][block_row]
                sectors[block_index * 1 + block_index * size].append(block[block_col][block_row])
        sectors[block_index * 1 + block_index * size].sort()


    for col in range(side_size):
        for row in range(side_size):
            possible_numbers = range(1, side_size + 1)
            numbers_found = []
            sectors_index = (row/size) * size + col/size

            # search for possible numbers for every empty Field (represented by 0 on the board)
            if board[col][row] == 0:
                for iter in range(side_size):
                    if board[col][iter] != 0:
                        numbers_found.append(board[col][iter])
                        try:
                            possible_numbers.remove(board[col][iter])
                        except:
                            pass
                    if board[iter][row] != 0:
                        numbers_found.append(board[iter][row])
                        try:
                            possible_numbers.remove(board[iter][row])
                        except:
                            pass
                if sectors[sectors_index] != []:
                    for nr in sectors[sectors_index]:
                        numbers_found.append(nr)
                        try:
                            possible_numbers.remove(nr)
                        except:
                            pass

                try:
                    chosen_number = np.random.choice(possible_numbers, 1)[0]
                    board[col][row] = chosen_number
                    sectors[sectors_index].append(chosen_number)
                except:
                    print "FAIL! no possibility"
                    pass
            #print board

    print board
def main():
    """Description of main()"""
    board = generateBoard(size = 3)
    print board


if __name__ == '__main__':
    main()