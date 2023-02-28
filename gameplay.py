import re
from os import system, name
import game_board


def clear():

    if name == 'nt':

        _ = system('cls')
    else:
        _ = system('clear')


def change_coords_to_corect(move, dimension):
    if len(move) != 2:
        return False
    dictionary = game_board.creat_move_dictionary(dimension)
    move = re.split('(\d+)', move.upper())
    move.remove('')
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


def if_neighbour_shot(board_for_player, dimension, coords):
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
        if board_for_player[elements[0]][elements[1]] == 'H':
            return [elements[0], elements[1]]
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


def place_ships(board_for_player, dimension):
    harbour = game_board.ship_harbour(dimension)
    player_fleet = []
    for ship in harbour:
        ship_number = ship['number']
        while ship_number > 0:
            ship_placment = []
            name = ship['name']
            game_board.print_game_board(board_for_player, dimension)
            print(f'Podaj koordynaty {name} ', end='')
            coords = input()
            if change_coords_to_corect(coords, dimension) == False:
                print("Podano złą składnie koordynatów")
            else:
                coords = change_coords_to_corect(coords, dimension)
                if board_for_player[coords[0]][coords[1]] == "X":
                    print("Już wybierałeś te koordynaty")
                elif is_collision(board_for_player, dimension, coords):
                    ship_placment.append([coords[0], coords[1]])
                    if ship['size'] > 1:
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
                        if plecement_direction.lower() == "h":
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
                    print("Nastąpiła kolizja wybierz inne miejsce swojego statku")
            player_fleet.append(
                {'name': name, 'coords': ship_placment, 'status': ship_placment})

    return board_for_player, player_fleet


def create_board_for_player(dimension):

    clear()

    board_for_player = game_board.creat_game_board(dimension)

    board_for_player, fleet = place_ships(board_for_player, dimension)

    return board_for_player, fleet
