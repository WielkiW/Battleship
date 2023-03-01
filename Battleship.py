import sys
import game_board
import gameplay
import graphix
import time
dimension = 5


def game_dev():

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

        graphix.clear()
        print('Player 1')
        print("Twoje statki:")
        game_board.print_game_board(board_for_player_1, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_1, dimension)
        value_win_player_1 = gameplay.shoot(fleet_for_player2, game_board_player_1,
                                            board_for_player_2, value_win_player_1, dimension)
        if value_win_player_1 == value_to_win:
            break

        graphix.clear()
        print('Player 2')
        print("Twoje statki:")
        game_board.print_game_board(board_for_player_2, dimension)
        print("Twoje strzały:")
        game_board.print_game_board(game_board_player_2, dimension)

        value_win_player_2 = gameplay.shoot(fleet_for_player1, game_board_player_2,
                                            board_for_player_1, value_win_player_2, dimension)

    if value_win_player_1 == value_to_win:
        print("Player 2 is a gdmn looser")
    else:
        print("Fck ya player 1")


def menu_battleship(dimension):

    menu_operation = 0

    board_for_player_1 = []
    board_for_player_2 = []
    player1_fleet = []
    player2_fleet = []

    while menu_operation != 5:
        graphix.clear()
        graphix.title()
        print("Witamy w naszej grze ")
        print("1. Graj")
        print("2. Ustawienia statków dla gracza 1")
        print("3. Ustawienia statków dla gracza 2")
        print('4. Opcje')
        print("5. EXIT")
        graphix.ship_graphic()
        match menu_operation:
            case 1:

                if board_for_player_1 == []:
                    print("Nie wypełniłeś pól statków")
                    time.sleep(3)
                    menu_operation = 2
                elif board_for_player_2 == []:
                    print("Nie wypełniłeś pól statków")
                    time.sleep(3)
                    menu_operation = 3

                else:
                    return [board_for_player_1, board_for_player_2, player1_fleet, player2_fleet]
            case 2:
                graphix.clear()
                print("Player 1")
                board_for_player_1, player1_fleet = gameplay.create_board_for_player(
                    dimension)
                menu_operation = 0
            case 3:
                graphix.clear()
                print("Player 2")
                board_for_player_2, player2_fleet = gameplay.create_board_for_player(
                    dimension)
                menu_operation = 0
            case 4:
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
            case _:
                try:
                    menu_operation = int(input("Wybierz opcję: "))

                except ValueError:
                    pass
    graphix.clear()
    print("Dziękujemy za grę.")

    sys.exit(0)


game_dev()
