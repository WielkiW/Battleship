import random
import gameplay
import game_board


def enemy_ai(dimension, player_board, ai_board, player_fleet, win, next_shoot, previous_shoot):
    value_to_win_ai = win
    shoot = 0
    if next_shoot == []:
        while shoot == 0:
            row = random.randint(0, dimension-1)
            column = random.randint(0, dimension-1)
            if ai_board[row][column] == 0:
                print(row, column)
                shoot = 1
                value_to_win_ai = gameplay.shoot(
                    player_fleet, ai_board, player_board, value_to_win_ai, [row, column])
            if player_board[row][column] == 'H':
                print(row, column)
            previous_shoot = [row, column]
    else:
        shoot_coordinates = next_shoot[0]
        print(shoot_coordinates)
        value_to_win_ai = gameplay.shoot(
            player_fleet, ai_board, player_board, value_to_win_ai, shoot_coordinates)

    return value_to_win_ai, previous_shoot


def check_for_next_shot(previous_shoot, ai_board, dimension, next_shoot):
    if ai_board[previous_shoot[0]][previous_shoot[1]] == 'H':
        rows_to_check = [previous_shoot[0]+1, previous_shoot[0]-1]
        columns_to_check = [previous_shoot[1]-1, previous_shoot[1]+1]
        for row in rows_to_check:
            if 0 <= row <= dimension-1 and ai_board[row][previous_shoot[1]] == 0:
                next_shoot.append([row, previous_shoot[1]])
        for column in columns_to_check:
            if 0 <= column <= dimension-1:
                next_shoot.append([previous_shoot[0], column])
    elif ai_board[previous_shoot[0]][previous_shoot[1]] == 'S':
        next_shoot.clear()

    return next_shoot


def check_line(ai_board, previous_shoot, next_shoot, dimension):
    if ai_board[previous_shoot[0]][previous_shoot[1]] == 'H':
        if 0 <= previous_shoot[0]+1 <= dimension or 0 <= previous_shoot[0]-1 <= dimension:
            if ai_board[previous_shoot[0]+1][previous_shoot[1]] == 'H' or ai_board[previous_shoot[0]-1][previous_shoot[1]] == 'H':
                next_shoot.clear()
                rows_to_check = [previous_shoot[0],
                                 previous_shoot[0]+1, previous_shoot[0]-1, previous_shoot[0]+2,  previous_shoot[0]-2]
                for row in rows_to_check:
                    if 0 <= row <= dimension - 1 and ai_board[row][previous_shoot[1]] == 0:
                        next_shoot.append([row, previous_shoot[1]])
        elif 0 <= previous_shoot[1]+1 <= dimension or 0 <= previous_shoot[1]-1 <= dimension:
            if ai_board[previous_shoot[0]][previous_shoot[1]+1] == 'H' or ai_board[previous_shoot[0]][previous_shoot[1]-1] == 'H':
                next_shoot.clear()
                columns_to_check = [previous_shoot[1], previous_shoot[1]+1,
                                    previous_shoot[1]-1, previous_shoot[1]+2, previous_shoot[1]-2]
                for column in columns_to_check and ai_board[previous_shoot[0]][column]:
                    if 0 <= row <= dimension - 1:
                        next_shoot.append([previous_shoot[0], column])
        next_shoot.pop(0)
    else:
        pass
    return next_shoot


def random_ship_placment(dimension, ai_board):
    ai_harbour = game_board.ship_harbour(dimension)
    ai_fleet = []
    for ship in ai_harbour:
        ship_number = ship['number']
        while ship_number > 0:
            ship_placment = []
            name = ship['name']
            placment = 0
            check = []
            while placment == 0:
                row = random.randint(0, dimension-1)
                column = random.randint(0, dimension-1)
                if ai_board[row][column] == 0:
                    placment = 1
                    if ship['size'] > 1:
                        ship_direction = ['h', 'v']
                        placment_direction = random.choice(ship_direction)
                        check = gameplay.ship_direction(placment_direction, ship_placment, ship, dimension, [
                            row, column], ai_board, check)
                    else:
                        ship_placment.append([row, column])
                        check = []
                        for block in ship_placment:
                            check.append(gameplay.is_collision(
                                ai_board, dimension, block))
                    if all(check):
                        ship_number -= 1
                        for block in ship_placment:
                            ai_board[block[0]][block[1]] = 'X'
                        ai_fleet.append(
                            {'name': name, 'coords': ship_placment, 'status': ship_placment})

    return ai_board, ai_fleet
