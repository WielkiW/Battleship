import sys
import game_board
import gameplay
import graphix
import time
import ai


def main():
    oponent = 'x'
    while oponent == 'x':
        oponent, dimension, boards_fleets = menu_battleship()
    if oponent == 'player':
        game_dev(dimension, boards_fleets)
    else:
        player_vs_cpu(dimension, boards_fleets)


def game_dev(dimension, boards_fleets):

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

        graphix.clear()
        print('Player 1')
        print("Twoje statki:")
        game_board.print_game_board(board_for_player_1, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_1, dimension)
        shoot_coords1 = False
        while shoot_coords1 == False:
            shoot_coords1 = input("Podaj koordynaty do stzału: ")
            shoot_coords1 = gameplay.change_coords_to_corect(
                shoot_coords1, dimension)
        value_win_player_1 = gameplay.shoot(fleet_for_player2, game_board_player_1,
                                            board_for_player_2, value_win_player_1,  shoot_coords1)
        if value_win_player_1 == value_to_win:
            break

        graphix.clear()
        print('Player 2')
        print("Twoje statki:")
        game_board.print_game_board(board_for_player_2, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_2, dimension)
        shoot_coords2 = False
        while shoot_coords2 == False:
            shoot_coords2 = input("Podaj koordynaty do stzały: ")
            shoot_coords2 = gameplay.change_coords_to_corect(
                shoot_coords2, dimension)
        value_win_player_2 = gameplay.shoot(fleet_for_player1, game_board_player_2,
                                            board_for_player_1, value_win_player_2,  shoot_coords2)

    if value_win_player_1 == value_to_win:
        print("Player 2 is a gdmn looser")
    else:
        print("Fck ya player 1")


def player_vs_cpu(dimension, boards_fleets):

    board_for_player_1 = boards_fleets[0]
    board_for_ai = boards_fleets[1]
    fleet_for_player1 = boards_fleets[2]
    fleet_ai = boards_fleets[3]

    game_board_player_1 = game_board.creat_game_board(dimension)
    game_board_ai = game_board.creat_game_board(dimension)

    value_to_win = game_board.shots_to_win(dimension)

    value_win_player_1 = 0
    value_win_ai = 0

    while value_win_player_1 != value_to_win or value_win_ai != value_to_win:

        graphix.clear()
        print('Player 1')
        print("Twoje statki:")
        game_board.print_game_board(board_for_player_1, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_1, dimension)
        shoot_coords1 = input("Podaj koordynaty do stzały: ")
        shoot_coords1 = gameplay.change_coords_to_corect(
            shoot_coords1, dimension)
        value_win_player_1 = gameplay.shoot(fleet_ai, game_board_player_1,
                                            board_for_ai, value_win_player_1, shoot_coords1)
        if value_win_player_1 == value_to_win:
            break

        graphix.clear()
        print('CPU')
        print("Statki CPU:")
        game_board.print_game_board(board_for_ai, dimension)
        print("Strzały CPU:")
        game_board.print_game_board(game_board_ai, dimension)
        time.sleep(3)
        value_win_ai = ai.enemy_ai(
            dimension, board_for_player_1, game_board_ai, fleet_for_player1, value_win_ai)
        time.sleep(3)

    if value_win_player_1 == value_to_win:
        print("AI is a gdmn looser")
    else:
        print("Fck ya player 1")


def menu_battleship():
    dimension = 5
    menu_operation = 0
    board_for_player_1 = []
    board_for_player_2 = []
    player1_fleet = []
    player2_fleet = []
    board_for_ai = []
    ai_fleet = []

    while menu_operation != 6:
        graphix.clear()
        graphix.title()
        print("Witamy w naszej grze ")
        print("1. Player vs Player")
        print('2. Player vs AI')
        print("3. Ustawienia statków dla gracza 1")
        print("4. Ustawienia statków dla gracza 2")
        print('5. Opcje')
        print("6. EXIT")

        graphix.ship_graphic()
        match menu_operation:
            case 1:

                if board_for_player_1 == []:
                    print("Nie wypełniłeś pól statków")
                    time.sleep(3)
                    menu_operation = 3
                elif board_for_player_2 == []:
                    print("Nie wypełniłeś pól statków")
                    time.sleep(3)
                    menu_operation = 4
                else:
                    return 'player', dimension, [board_for_player_1, board_for_player_2, player1_fleet, player2_fleet]
            case 3:
                graphix.clear()
                print("Player 1")
                board_for_player_1, player1_fleet = gameplay.create_board_for_player(
                    dimension)
                menu_operation = 0
            case 4:
                graphix.clear()
                print("Player 2")
                board_for_player_2, player2_fleet = gameplay.create_board_for_player(
                    dimension)
                menu_operation = 0
            case 5:
                new_dimension = 0
                while new_dimension < 5:
                    try:
                        new_dimension = int(
                            input("Podaj wymiar planszy (5-10): "))
                    except ValueError:
                        print('Wymiar musi być cyfrą')
                    else:
                        if new_dimension <= 10:
                            dimension = new_dimension
                            board_for_player_1 = []
                            board_for_player_2 = []
                        else:
                            new_dimension = 0
                menu_operation = 0
            case 2:
                if board_for_player_1 == []:
                    print("Nie wypełniłeś pól statków")
                    time.sleep(3)
                    menu_operation = 3
                else:
                    oponent = 'cpu'
                    board_for_ai = game_board.creat_game_board(dimension)
                    print(board_for_ai)
                    board_for_ai, ai_fleet = ai.random_ship_placment(
                        dimension, board_for_ai)
                    print(board_for_ai)
                    return 'cpu', dimension, [board_for_player_1, board_for_ai, player1_fleet, ai_fleet]
            case _:
                try:
                    menu_operation = int(input("Wybierz opcję: "))
                except ValueError:
                    pass


main()
