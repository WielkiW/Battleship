import sys
from os import system, name
import time
import game_board
import gameplay
import graphix


def game_dev():

    dimension = 5

    boards_fleets = menu_battleship(dimension)

    board_for_player_1 = boards_fleets[0]
    board_for_player_2 = boards_fleets[1]
    fleet_for_player1 = boards_fleets[2]
    fleet_for_player2 = boards_fleets[3]

    game_board_player_1 = game_board.creat_game_board(dimension)
    game_board_player_2 = game_board.creat_game_board(dimension)

    value_to_win = game_board.shots_to_win(dimension)

    value_win_player_1 = 0
    value_win_player_2 = 0

    while value_win_player_1 != value_to_win or value_win_player_2 != value_to_win:

        clear()
        print('Player 1')
        print("Twoje statki:")
        game_board.print_game_board(board_for_player_1, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_1, dimension)

        shoot_coords = input("Podaj koordynaty do stzały: ")

        shoot_coords = gameplay.change_coords_to_corect(
            shoot_coords, dimension)

        for i in range(len(fleet_for_player2)):
            new_cord = []
            for item in fleet_for_player2[i]['status']:
                if item[0] == shoot_coords[0] and item[1] == shoot_coords[1]:
                    game_board_player_1 = game_board.change_board(
                        game_board_player_1, shoot_coords[0], shoot_coords[1], "H")
                    item = 'H'
                    value_win_player_1 += 1
                elif board_for_player_2[shoot_coords[0]][shoot_coords[1]] == 0:
                    game_board_player_1 = game_board.change_board(
                        game_board_player_1, shoot_coords[0], shoot_coords[1], "M")
                new_cord.append(item)
            fleet_for_player2[i]['status'] = new_cord
        for i in range(len(fleet_for_player2)):
            if all(element == 'H' for element in fleet_for_player2[i]['status']):
                for coordinates in fleet_for_player2[i]['coords']:
                    game_board_player_1 = game_board.change_board(
                        game_board_player_1, coordinates[0], coordinates[1], "S")

        clear()
        print('Player 2')
        print("Twoje statki:")
        game_board.print_game_board(board_for_player_2, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_2, dimension)

        shoot_coords = input("Podaj koordynaty do stzały: ")

        shoot_coords = gameplay.change_coords_to_corect(
            shoot_coords, dimension)

        for i in range(len(fleet_for_player1)):
            new_cord = []
            for item in fleet_for_player1[i]['status']:
                if item[0] == shoot_coords[0] and item[1] == shoot_coords[1]:
                    game_board_player_2 = game_board.change_board(
                        game_board_player_2, shoot_coords[0], shoot_coords[1], "H")
                    item = 'H'
                    value_win_player_2 += 1
                elif board_for_player_1[shoot_coords[0]][shoot_coords[1]] == 0:
                    game_board_player_2 = game_board.change_board(
                        game_board_player_2, shoot_coords[0], shoot_coords[1], "M")
                new_cord.append(item)
            fleet_for_player1[i]['status'] = new_cord
            for i in range(len(fleet_for_player1)):
                if all(element == 'H' for element in fleet_for_player1[i]['status']):
                    for coordinates in fleet_for_player1[i]['coords']:
                        game_board_player_2 = game_board.change_board(
                            game_board_player_2, coordinates[0], coordinates[1], "S")
    if value_win_player_1 == value_to_win:
        print("Player 2 is a gdmn looser")
    else:
        print("Fck ya player 1")


def menu_battleship(dimension):

    menu_operation = 0
    dimension = 5
    ship_number = 4

    board_for_player_1 = []
    board_for_player_2 = []
    player1_fleet = []
    player2_fleet = []

    while menu_operation != 4:
        graphix.title()
        print("Witamy w naszej grze ")
        print("1. Graj")
        print("2. Ustawienia statków dla gracza 1")
        print("3. Ustawienia statków dla gracza 2")
        print("4. EXIT")
        graphix.ship_graphic()
        match menu_operation:
            case 1:
                if board_for_player_1 == []:
                    print("Nie wypełniłeś pól statków")
                    menu_operation = 2
                elif board_for_player_2 == []:
                    print("Nie wypełniłeś pól statków")
                    menu_operation = 3
                else:
                    return [board_for_player_1, board_for_player_2, player1_fleet, player2_fleet]
            case 2:

                board_for_player_1, player1_fleet = gameplay.create_board_for_player(
                    dimension)
                menu_operation = 0
            case 3:

                board_for_player_2, player2_fleet = gameplay.create_board_for_player(
                    dimension)
                menu_operation = 0
            case _:
                try:
                    menu_operation = int(input("Wybierz opcję: "))
                except ValueError:
                    pass

        clear()
    print("Dziękujemy za grę.")

    sys.exit(0)


def clear():

    if name == 'nt':

        _ = system('cls')
    else:
        _ = system('clear')


game_dev()
