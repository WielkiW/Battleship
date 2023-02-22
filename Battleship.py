import sys
import re
from os import system, name


def clear():

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


def place_ships_2_blocks(board_for_player, dimension, ship_number):

    ship_meter_for_2_block = 0

    while ship_meter_for_2_block < ship_number:

        print_game_board(board_for_player, dimension)
        coords = input("Podaj koordynaty swojego statku 2 blockowego: ")
        if change_coords_to_corect(coords, dimension) == False:
            print("Podano złą składnie koordynatów")
        else:
            coords = change_coords_to_corect(coords, dimension)
            if board_for_player[coords[0]][coords[1]] == "X":
                print("Już wybierałeś te koordynaty")
            elif is_collision(board_for_player, dimension, coords):
                plecement_direction = input(
                    "Podaj kierunek statku 2 blockowego: (horizontal/vertical) [H/V]")
                if plecement_direction.lower() == "v" and (coords[0] + 1 < dimension or coords[0] - 1 >= 0):
                    if coords[0] + 1 < dimension and is_collision(board_for_player, dimension, (coords[0] + 1, coords[1])):
                        board_for_player[coords[0]+1][coords[1]] = "X"
                    elif is_collision(board_for_player, dimension, (coords[0] - 1, coords[1])):
                        board_for_player[coords[0]-1][coords[1]] = "X"
                elif plecement_direction.lower() == "h" and (coords[1] + 1 <= dimension or coords[1] - 1 >= 0):
                    if coords[1] + 1 < dimension and is_collision(board_for_player, dimension, (coords[0], coords[1]+1)):
                        board_for_player[coords[0]][coords[1]+1] = "X"
                    elif is_collision(board_for_player, dimension, (coords[0], coords[1]-1)):
                        board_for_player[coords[0]][coords[1]-1] = "X"
                board_for_player[coords[0]][coords[1]] = "X"
                ship_meter_for_2_block += 1
            else:
                print("Nastąpiła kolizja wybierz inne miejsce swojego statku")

    return board_for_player


def place_ships_1_block(board_for_player, dimension, ship_number):

    ship_meter_for_1_block = 0

    while ship_meter_for_1_block < ship_number:

        print_game_board(board_for_player, dimension)

        coords = input("Podaj koordynaty swojego statku 1 blockowego: ")
        if change_coords_to_corect(coords, dimension) == False:
            print("Podano złą składnie koordynatów")
        else:
            coords = change_coords_to_corect(coords, dimension)
        if is_collision(board_for_player, dimension, coords):
            if board_for_player[coords[0]][coords[1]] == "X":
                print("Już wybierałeś te koordynaty")
            else:
                board_for_player[coords[0]][coords[1]] = "X"
                ship_meter_for_1_block += 1
        else:
            print("Nastąpiła kolizja wybierz inne miejsce swojego statku")

    return board_for_player


def create_board_for_player_1(dimension, ship_number):

    board_for_player = creat_game_board(dimension)

    board_for_player = place_ships_2_blocks(
        board_for_player, dimension, ship_number/2)

    board_for_player = place_ships_1_block(
        board_for_player, dimension, ship_number)

    return [board_for_player]


def create_board_for_player_2():

    clear()

    return [1, 2, 3, 4, 5, 6]


def menu_battleship():

    menu_operation = 0
    dimension = 10
    ship_number = 4

    board_for_player_1 = []
    board_for_player_2 = []

    while menu_operation != 4:

        clear()

        print("Witamy w naszej grze :)")
        print("1. Graj")
        print("2. Ustawienia statków dla gracza 1")
        print("3. Ustawienia statków dla gracza 2")
        print("4. EXIT")

        menu_operation = int(input("Wybierz opcję: "))

        if menu_operation == 1:
            return [board_for_player_1, board_for_player_2]
        elif menu_operation == 2:
            board_for_player_1 = create_board_for_player_1(
                dimension, ship_number)
        elif menu_operation == 3:
            board_for_player_2 = create_board_for_player_2(dimension)

    print("Dziękujemy za grę.")
    sys.exit(0)


menu_battleship()
