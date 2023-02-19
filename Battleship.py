import sys
from os import system, name

def clear():
 
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

#def create_board_for_player_1():
#def create_board_for_player_2():

def menu_battleship():
    print("Witamy w naszej grze :)")
    print("1. Graj")
    print("2. Ustawienia statków dla gracza 1")
    print("3. Ustawienia statków dla gracza 2")
    print("4. EXIT")
    menu_operation = int(input("Wybierz opcję: "))
    while  1 <= menu_operation <= 3:
        if menu_operation == 1:
            print("gramy")
            #return #board dla gracza 1 i dla gracza 2
        elif menu_operation == 2:
            print("plansza gr1")
            #create_board_for_player_1()
        elif menu_operation == 3:
            print("plansza gr2")
            #create_board_for_player_2
    if menu_operation == 4:
        print("Dziękujemy za grę.")
        sys.exit(0)
    



clear()
menu_battleship()