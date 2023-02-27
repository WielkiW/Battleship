import sys
from os import system, name
import time
import game_board
import gameplay
import graphix


def game_dev():

    dimension = 5

    boards = menu_battleship(dimension)

    board_for_player_1 = boards[0]
    board_for_player_2 = boards[1]

    game_board_player_1 = game_board.creat_game_board(dimension)
    game_board_player_2 = game_board.creat_game_board(dimension)

    value_to_win = game_board.shots_to_win(dimension)

    value_win_player_1 = 0
    value_win_player_2 = 0

    while value_win_player_1 != value_to_win or value_win_player_2 != value_to_win:

        clear()

        print("Twoje statki:")
        game_board.print_game_board(board_for_player_1, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_1, dimension)

        shoot_coords = input("Podaj koordynaty do stzały: ")

        shoot_coords = gameplay.change_coords_to_corect(
            shoot_coords, dimension)

        if board_for_player_2[shoot_coords[0]][shoot_coords[1]] == "X":
            game_board_player_1 = game_board.change_board(
                game_board_player_1, shoot_coords[0], shoot_coords[1], "H")
            if gameplay.is_collision(board_for_player_2, dimension, shoot_coords):
                game_board_player_1 = game_board.change_board(
                    game_board_player_1, shoot_coords[0], shoot_coords[1], "S")
            else:
                neighbour_coords = gameplay.if_neighbour_shot(
                    game_board_player_1, dimension, shoot_coords)
                if neighbour_coords != False:
                    game_board_player_1 = game_board.change_board(
                        game_board_player_1, neighbour_coords[0], neighbour_coords[1], "S")
                    game_board_player_1 = game_board.change_board(
                        game_board_player_1, shoot_coords[0], shoot_coords[1], "S")

            clear()

            print("Twoje statki:")
            game_board.print_game_board(board_for_player_1, dimension)
            print("Twoje strzały:")
            game_board.print_game_board(game_board_player_1, dimension)
            print("Strzał trafiony")
            time.sleep(5)
            value_win_player_1 += 1
            if value_win_player_1 == value_to_win:
                break
        elif board_for_player_2[shoot_coords[0]][shoot_coords[1]] == "0":
            game_board_player_1 = game_board.change_board(
                game_board_player_1, shoot_coords[0], shoot_coords[1], "M")
            clear()

            print("Twoje statki:")
            game_board.print_game_board(board_for_player_1, dimension)
            print("Twoje strzały:")
            game_board.print_game_board(game_board_player_1, dimension)
            print("Strzał nietrafiony")
            time.sleep(5)

        clear()

        print("Twoje statki:")
        game_board.print_game_board(board_for_player_2, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_2, dimension)

        shoot_coords = input("Podaj koordynaty do stzały: ")

        shoot_coords = gameplay.change_coords_to_corect(
            shoot_coords, dimension)

        if board_for_player_1[shoot_coords[0]][shoot_coords[1]] == "X":
            game_board_player_2 = game_board.change_board(
                game_board_player_2, shoot_coords[0], shoot_coords[1], "H")
            if gameplay.is_collision(board_for_player_1, dimension, shoot_coords):
                game_board_player_2 = game_board.change_board(
                    game_board_player_2, shoot_coords[0], shoot_coords[1], "S")
            else:
                neighbour_coords = gameplay.if_neighbour_shot(
                    game_board_player_2, dimension, shoot_coords)
                if neighbour_coords != False:
                    game_board_player_2 = game_board.change_board(
                        game_board_player_2, neighbour_coords[0], neighbour_coords[1], "S")
                    game_board_player_2 = game_board.change_board(
                        game_board_player_2, shoot_coords[0], shoot_coords[1], "S")
            value_win_player_2 += 1
            clear()
            print("Twoje statki:")
            game_board.print_game_board(board_for_player_1, dimension)
            print("Twoje strzały:")
            game_board.print_game_board(game_board_player_1, dimension)
            if value_win_player_2 == value_to_win:
                break
            print("Strzał trafiony")
            time.sleep(5)
        elif board_for_player_1[shoot_coords[0]][shoot_coords[1]] == "0":
            game_board_player_2 = game_board.change_board(
                game_board_player_2, shoot_coords[0], shoot_coords[1], "M")
            clear()
            print("Twoje statki:")
            game_board.print_game_board(board_for_player_1, dimension)
            print("Twoje strzały:")
            game_board.print_game_board(game_board_player_1, dimension)
            print("Strzał nietrafiony")
            time.sleep(5)
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
                    return [board_for_player_1, board_for_player_2]
            case 2:
                player = 1
                board_for_player_1 = create_board_for_player(dimension, player)
                menu_operation = 0
            case 3:
                player = 2
                board_for_player_2 = create_board_for_player(dimension, player)
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


def create_board_for_player(dimension, player):

    clear()

    board_for_player = game_board.creat_game_board(dimension)

    board_for_player = gameplay.place_ships(
        board_for_player, dimension, player)

    return board_for_player


game_dev()
