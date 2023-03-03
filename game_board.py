def creat_game_board(dimension):
    game_board = []
    row = []
    i = 1
    j = 1
    while i <= dimension:
        while j <= dimension:
            row.append(0)
            j += 1
        game_board.append(row)
        row = []
        j = 1
        i += 1
    return game_board


def change_board(board, coord_y, coord_x, sign):
    board[coord_y][coord_x] = sign
    return board


def print_game_board(game_board, dimension):
    print('')
    i = 1
    while i <= dimension-1:
        print(' ', i, end='')
        i += 1
    print(' ', dimension)
    for i, element in zip(range(65, 66+dimension), game_board):
        print(chr(i), end=' ')
        for j in element:
            print(j, end='  ')
        print('')
    print('')


def creat_move_dictionary(dimension):
    move_dictionary = {}
    for i in range(dimension):
        move_dictionary[chr(65+i)] = i
    return move_dictionary


def ship_harbour(dimension):
    match dimension:
        case 5:
            return (
                {'name': 'dwumasztowiec', 'size': 2, 'number': 2},
                {'name': 'jednomasztowiec', 'size': 1, 'number': 4},)
        case 6:
            return (
                {'name': 'dwumasztowiec', 'size': 2, 'number': 3},
                {'name': 'jednomasztowiec', 'size': 1, 'number': 4},)
        case 7:
            return (
                {'name': 'dwumasztowiec', 'size': 2, 'number': 3},
                {'name': 'jednomasztowiec', 'size': 1, 'number': 4},)
        case 8:
            return (
                {'name': 'trzymasztowiec', 'size': 3, 'number': 1},
                {'name': 'dwumasztowiec', 'size': 2, 'number': 3},
                {'name': 'jednomasztowiec', 'size': 1, 'number': 4},)
        case 9:
            return (
                {'name': 'trzymasztowiec', 'size': 3, 'number': 2},
                {'name': 'dwumasztowiec', 'size': 2, 'number': 3},
                {'name': 'jednomasztowiec', 'size': 1, 'number': 4},)
        case 10:
            return (
                {'name': 'czteromasztowiec', 'size': 4, 'number': 1},
                {'name': 'trzymasztowiec', 'size': 3, 'number': 2},
                {'name': 'dwumasztowiec', 'size': 2, 'number': 3},
                {'name': 'jednomasztowiec', 'size': 1, 'number': 4},)
        case _:
            return 'Invalid value'


def shots_to_win(dimension):
    match dimension:
        case 5:
            return (8)
        case 6:
            return (10)
        case 7:
            return (10)
        case 8:
            return (13)
        case 9:
            return (16)
        case 10:
            return (20)
        case _:
            return 'Invalid value'


board = creat_game_board(10)
print_game_board(board, 10)
