import sys
import re
import re
from os import system, name


def clear():

    if name == 'nt':

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


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


def creat_move_dictionary(dimension):
    move_dictionary = {}
    for i in range(dimension):
        move_dictionary[chr(65+i)] = i
    return move_dictionary


def change_coords_to_corect(move, dimension):
    dictionary = creat_move_dictionary(dimension)
    move = re.split('(\d+)', move.upper())
    move.remove('')
    if len(move) != 2:
        return False
    try:
        int(move[0])
    except:
        if (move[0]) in dictionary.keys() and int(move[1]) <= dimension:
            return (dictionary[move[0]], int(move[1])-1)
        else:
            return False
    else:
        if int(move[0]) <= dimension and (move[1]) in dictionary.keys():
            return (dictionary[move[1]], int(move[0])-1)
        else:
            return False


def is_collision(board_for_player, dimension, coords):
    row = coords[0]
    column = coords[1]
    funcs = [(row-1, column),
             (row, column + 1),
             (row+1, column),
             (row, column-1)]
    neighbours = []
    for func in funcs:
        if dimension > func[0] >= 0 and dimension > func[1] >= 0:
            neighbours.append([func[0], func[1]])
    for elements in neighbours:
        if board_for_player[elements[0]][elements[1]] == 'X':
            return False
    return True


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


def place_ships(board_for_player, dimension):
    harbour = ship_harbour(dimension)
    for ship in harbour:
        ship_number = ship['number']
        while ship_number > 0:
            ship_placment = []
            name = ship['name']
            print_game_board(board_for_player, dimension)
            print(f'Podaj koordynaty {name} ', end='')
            coords = input()
            if change_coords_to_corect(coords, dimension) == False:
                print("Podano złą składnie koordynatów")
            else:
                coords = change_coords_to_corect(coords, dimension)
                if board_for_player[coords[0]][coords[1]] == "X":
                    print("Już wybierałeś te koordynaty")
                elif is_collision(board_for_player, dimension, coords):
                    if ship['size'] > 1:
                        ship_placment.append([coords[0], coords[1]])
                        plecement_direction = input(
                            "Podaj kierunek statku 2 blockowego: (horizontal/vertical) [H/V]")
                        if plecement_direction.lower() == "v":
                            if coords[0] + ship['size'] - 1 < dimension:
                                for i in range(1, ship['size']):
                                    ship_placment.append(
                                        [coords[0] + i, coords[1]])
                            else:
                                for i in range(1, ship['size']):
                                    ship_placment.append(
                                        [coords[0] - i, coords[1]])
                            check = []
                            for block in ship_placment:
                                check.append(is_collision(
                                    board_for_player, dimension, block))
                            if all(check):
                                ship_number -= 1
                                for block in ship_placment:
                                    board_for_player[block[0]][block[1]] = 'X'
                            else:
                                print('Invalid move')

                        elif plecement_direction.lower() == "h":
                            if coords[1] + ship['size'] - 1 < dimension:
                                for i in range(1, ship['size']):
                                    ship_placment.append(
                                        [coords[0], coords[1]+i])
                            else:
                                for i in range(1, ship['size']):
                                    ship_placment.append(
                                        [coords[0], coords[1]-i])
                            check = []
                            for block in ship_placment:
                                check.append(is_collision(
                                    board_for_player, dimension, block))
                            if all(check):
                                ship_number -= 1
                                for block in ship_placment:
                                    board_for_player[block[0]][block[1]] = 'X'
                            else:
                                print('Invalid move')
                        else:
                            print('Invalid move')
                    else:
                        board_for_player[coords[0]][coords[1]] = 'X'
                        ship_number -= 1

                else:
                    print("Nastąpiła kolizja wybierz inne miejsce swojego statku")

    return board_for_player


def create_board_for_player_1(dimension):

    clear()

    board_for_player = creat_game_board(dimension)

    board_for_player = place_ships(board_for_player, dimension)

    return board_for_player


def create_board_for_player_2(dimension):

    clear()

    board_for_player = creat_game_board(dimension)

    board_for_player = place_ships(board_for_player, dimension)

    return board_for_player


def change_board(board, coord_x, coord_y, sign):
    board[coord_y][coord_x] = sign
    return board


def menu_battleship(dimension):

    menu_operation = 0
    dimension = 5
    ship_number = 4

    board_for_player_1 = []
    board_for_player_2 = []

    while menu_operation != 4:

        # clear()

        print("Witamy w naszej grze :)")
        print("1. Graj")
        print("2. Ustawienia statków dla gracza 1")
        print("3. Ustawienia statków dla gracza 2")
        print("4. EXIT")

        menu_operation = int(input("Wybierz opcję: "))

        if menu_operation == 1:
            if board_for_player_1 == []:
                print("Nie wypełniłeś pól statków")
                menu_operation = 2
            elif board_for_player_2 == []:
                print("Nie wypełniłeś pól statków")
                menu_operation = 3
            else:
                return [board_for_player_1, board_for_player_2]
        if menu_operation == 2:
            board_for_player_1 = create_board_for_player_1(dimension)
        if menu_operation == 3:
            board_for_player_2 = create_board_for_player_2(dimension)

    print("Dziękujemy za grę.")

    sys.exit(0)


def game_dev():

    dimension = 5

    boards = menu_battleship(dimension)

    board_for_player_1 = boards[0]
    board_for_player_2 = boards[1]

    game_board_player_1 = creat_game_board(dimension)
    game_board_player_2 = creat_game_board(dimension)

    value_to_win = shots_to_win(dimension)

    value_win_player_1 = 0
    value_win_player_2 = 0

    while value_win_player_1 != value_to_win or value_win_player_2 != value_to_win:

        # clear()

        print("Twoje statki:")
        print_game_board(board_for_player_1, dimension)
        print("Twoje strzały:")
        print_game_board(game_board_player_1, dimension)

        shoot_coords = input("Podaj koordynaty do stzały: ")

        shoot_coords = change_coords_to_corect(shoot_coords, dimension)

        if board_for_player_2[shoot_coords[0]][shoot_coords[1]] == "X":
            game_board_player_1 = change_board(
                game_board_player_1, shoot_coords[0], shoot_coords[1], "H")
            print("Strzał trafiony")
            value_win_player_1 += 1
        elif board_for_player_2[shoot_coords[0]][shoot_coords[1]] == "0":
            game_board_player_1 = change_board(
                game_board_player_1, shoot_coords[0], shoot_coords[1], "M")
            print("Strzał nietrafiony")

        # clear()

        print("Twoje statki:")
        print_game_board(board_for_player_2, dimension)
        print("Twoje strzały:")
        print_game_board(game_board_player_2, dimension)

        shoot_coords = input("Podaj koordynaty do stzały: ")

        shoot_coords = change_coords_to_corect(shoot_coords, dimension)

        if board_for_player_1[shoot_coords[0]][shoot_coords[1]] == "X":
            game_board_player_2 = change_board(
                game_board_player_2, shoot_coords[0], shoot_coords[1], "H")
            value_win_player_2 += 1
            print("Strzał trafiony")
        elif board_for_player_1[shoot_coords[0]][shoot_coords[1]] == "0":
            game_board_player_2 = change_board(
                game_board_player_2, shoot_coords[0], shoot_coords[1], "M")
            print("Strzał nietrafiony")


game_dev()
