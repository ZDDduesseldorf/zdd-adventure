"""This starts the adventure
"""
import os
import json
import time
import zdd_adventure.save as save
import zdd_adventure.change_place as change_place
from zdd_adventure.graphics import countdown, slow_print

end_game = False


def start():
    print(">>>> Loading Data...")
    data_saves = save.initialize_saves()
    accounts = list(data_saves.keys())
    while True:
        print("\n\nChoose your Game-stats\n\n0: New Game")
        for i, account in enumerate(accounts):
            print(f"{i+1} {account}")
        my_game = input("\nInsert your Game:")
        if my_game.strip() == "0":
            print("Welcome newcommer! \nFirst tell me your Name") # falls das in dritte form geschrieben werden soll bitte korrigieren
            name = ""
            while (name == "") or (name in accounts):
                name = input("Enter your name: ")
            save.create_new_player(data_saves, name)
            break
        if my_game.isnumeric() and int(my_game) <= len(accounts):
            name = accounts[(int(my_game)-1)]
            save.load_player_data(data_saves, name)
            print(f'Welcome back {name}!')
            break

    data_current = data_saves[name]
    while not end_game:
        os.system('cls')
        change_place.floor_rooms[data_current["floor"]][data_current["room"]]["func"](data_current)
        data_current = change_place.change_place(data_current)
        save.save_data(data_saves, data_current)


if __name__ == '__main__':
    start()
