import random
import gameplay
import game_board


def enemy_ai(dimension, player_board, ai_board, player_fleet, value_to_win_ai):
    shoot = 0
    next_shot = []
    if next_shot == []:
        while shoot == 0:
            row = random.randint(0, dimension-1)
            column = random.randint(0, dimension-1)
            if ai_board[row][column] == 0:
                shoot = 1
                value_to_win_ai = gameplay.shoot(
                    player_fleet, ai_board, player_board, value_to_win_ai, [row, column])
            if player_board[row][column] == 'H':
                to_check = [[row+1, column], [row-1, column],
                            [row, column-1], [row, column+1]]
                for item in to_check:
                    if ai_board[item[0]][item[1]] == 0:
                        next_shot.append(item)
                previous_shot = [[row][column]]
    else:
        shoot_coordinates = next_shot[0]
        value_to_win_ai = gameplay.shoot(
            player_fleet, ai_board, player_board, value_to_win_ai, shoot_coordinates)
        if player_board[shoot_coordinates[0]][shoot_coordinates[1]] == 'H':
            if previous_shot[0] == shoot_coordinates[0]:
                next_shot.clear()
                next_shot.append([previous_shot[0]-1, shoot_coordinates[1]])
                next_shot.append([previous_shot[0]-2, shoot_coordinates[1]])
                next_shot.append([previous_shot[0]+1, shoot_coordinates[1]])
                next_shot.append([previous_shot[0]+2, shoot_coordinates[1]])
            elif player_board[shoot_coordinates[0]][shoot_coordinates[1]] == 'S':
                next_shot.clear()
            else:
                next_shot.pop(0)


def random_ship_placment(dimension, ai_board):
    ai_harbour = game_board.ship_harbour(dimension)
    ai_fleet = []
    for ship in ai_harbour:
        ship_number = ship['number']
        while ship_number > 0:
            ship_placment = []
            name = ship['name']
            placment = 0
            while placment == 0:
                row = random.randint(0, dimension-1)
                column = random.randint(0, dimension-1)
                if ai_board[row][column] == 0:
                    placment = 1
                    if ship['size'] > 1:
                        placment_direction = random.choice('h', 'v')
                        check = gameplay.ship_direction(placment_direction, ship_placment, ship, dimension, [
                            row, column], ai_board)
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
