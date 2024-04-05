import os

import modset_factions
from modset_json import read_json_return

from select_random import select_random_factions
from select_random import select_random_factions_multiple

from logging import log_message

def return_faction_choices():

    os.system('cls')

    setting_modsets = read_json_return("settings", "modsets")

    if (setting_modsets == "random"):
        modset = modset_factions.grab_random_modset("modsets", "modsets", random_modset=setting_modsets)
    elif (setting_modsets == "random_multiple"):
        modset = read_json_return("modsets", "modsets")
    else:
        modset = setting_modsets

    log_message(-1, f"Modset was {modset}")

    setting_choices = read_json_return("settings", "choices")

    collections = select_random_factions_multiple(modset, setting_choices)
    modsets = collections[2]

    for message in modsets:
        if (isinstance(message, int)):
            log_message(-1, f"\nChoice {message + 1}")
        else:
            log_message(-1, f"\033[F{message[0]}")

    log_message(-1, "\nThese factions require:")
    for collection in collections[1]:
        log_message(-1, collection)

return_faction_choices()