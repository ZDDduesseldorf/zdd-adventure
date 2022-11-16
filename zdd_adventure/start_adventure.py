"""This starts the adventure
"""
import os
import zdd_adventure.save as save
import zdd_adventure.change_place as change_place

end_game = False

def start():
    print(">>>> Loading Data...")
    # Spieldaten laden
    data_saves = save.initialize_saves()
    accounts = list(data_saves.keys())
    my_game = ""
    while my_game == "":
        print("\n\nChoose your Game-stats\n\n0: New Game")
        for i in range(len(accounts)):
            print((i+1), accounts[i])
        my_game = input("\nInsert your Game:")
        if my_game.isnumeric():
            if not int(my_game) <= len(accounts):
                my_game = ""
        else:
            my_game = ""
    name = ""
    if my_game == "0":
        print("Welcome newcommer! \nFirst tell me your Name") # falls das in dritte form geschrieben werden soll bitte korrigieren
        while (name == "") or (name in accounts):
            name = input("Enter your name: ")
        save.create_new_player(data_saves, name)
    else:
        name = accounts[(int(my_game)-1)]
        print(f'Welcome back {name}!')
    save.load_player_data(data_saves, name)
    data_current = data_saves[name]
    while not end_game:
        os.system('cls')
        change_place.floor_rooms[data_current["floor"]][data_current["room"]]["func"](data_current)
        data_current = change_place.change_place(data_current)
        save.save_data(data_saves, data_current)


if __name__ == '__main__':
    start()