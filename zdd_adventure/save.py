# -*- coding: utf-8 -*-
import json
import os


_filename_json_empty = os.path.join(os.path.dirname(__file__), "player_data_empty.json")
_filename_json_saves = os.path.join(os.path.dirname(__file__), "player_data.json")


def load_data(filename: str):
    """Opening JSON file.
    """
    f = open(filename, "r")
    # returns JSON object as a dictionary
    data = json.load(f)
    f.close()
    return data


def initialize_saves():
    try:
        data_saves = load_data(_filename_json_saves)
        return data_saves
    except FileNotFoundError:
        print("No saved games found.")
        return dict()


def load_player_data(data_saves, name):
    """Load player data, if available"""
    try:
        player_data = data_saves[name]
        return player_data
    except:
        print(f"No data found for player name {name}.")
        print("Will create new player.")
        return create_new_player(data_saves, name)


def save_data(data_saves, data_current):
    name = data_current["name"]
    data_saves[name] = data_current
    with open(_filename_json_saves, 'w') as f:
        json.dump(data_save, f)


def create_new_player(data_saves, name):
    # Check if saves exist or not
    data_saves[name] = load_data(_filename_json_empty)
    data_saves[name]["name"] = name
    return data_saves
