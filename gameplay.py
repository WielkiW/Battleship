import re
import game_board
import time


def shoot(oponent_fleet, player_board, oponent_board, win, shoot_coords):
    player_value_to_win = win
    for i in range(len(oponent_fleet)):
        new_cord = []
        for item in oponent_fleet[i]['status']:
            if item[0] == shoot_coords[0] and item[1] == shoot_coords[1]:
                if oponent_board[shoot_coords[0]][shoot_coords[1]] == 'X':
                    player_board = game_board.change_board(
                        player_board, shoot_coords[0], shoot_coords[1], "H")
                    item = 'H'
                    player_value_to_win += 1
                    print("Trafiony")
                    time.sleep(3)
            new_cord.append(item)
        oponent_fleet[i]['status'] = new_cord
    for i in range(len(oponent_fleet)):
        if all(element == 'H' for element in oponent_fleet[i]['status']):
            oponent_fleet[i]['status'] = 'S'
            for coordinates in oponent_fleet[i]['coords']:
                player_board = game_board.change_board(
                    player_board, coordinates[0], coordinates[1], "S")
            print("Trafiony zatopiony")
            time.sleep(5)
    if oponent_board[shoot_coords[0]][shoot_coords[1]] == 0:
        player_board = game_board.change_board(
            player_board, shoot_coords[0], shoot_coords[1], "M")
        print("Pudło")
        time.sleep(3)
    return player_value_to_win


def change_coords_to_corect(move, dimension):
    if len(move) < 2:
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


def ship_direction(plecement_direction, ship_placment, ship, dimension, coords, board_for_player, check):
    match plecement_direction.lower():
        case "v":
            ship_placment.append([coords[0], coords[1]])
            if coords[0] + ship['size'] - 1 < dimension:
                for i in range(1, ship['size']):
                    ship_placment.append([coords[0] + i, coords[1]])
            else:
                for i in range(1, ship['size']):
                    ship_placment.append([coords[0] - i, coords[1]])
            check = []
            for block in ship_placment:
                check.append(is_collision(
                    board_for_player, dimension, block))
        case "h":
            ship_placment.append([coords[0], coords[1]])
            if coords[1] + ship['size'] - 1 < dimension:
                for i in range(1, ship['size']):
                    ship_placment.append([coords[0], coords[1]+i])
            else:
                for i in range(1, ship['size']):
                    ship_placment.append([coords[0], coords[1]-i])
            check = []
            for block in ship_placment:
                check.append(is_collision(
                    board_for_player, dimension, block))
        case _:
            check = [False]
    return check


def place_ships(board_for_player, dimension):
    harbour = game_board.ship_harbour(dimension)
    player_fleet = []
    check = []
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
                    if ship['size'] > 1:
                        plecement_direction = input(
                            "Podaj kierunek statku: (horizontal/vertical) [H/V]")
                        check = ship_direction(
                            plecement_direction, ship_placment, ship, dimension, coords, board_for_player, check)
                    else:
                        ship_placment.append([coords[0], coords[1]])
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
    board_for_player = game_board.creat_game_board(dimension)
    board_for_player, fleet = place_ships(board_for_player, dimension)
    return board_for_player, fleet
