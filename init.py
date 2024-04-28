import os

from modset_json import read_json_return
from modset_json import read_json_return_dict

from logging import log_message

from faction import return_faction_choices
from faction import display_factions
from faction import grab_modset

def init(modset=""):
    os.system('cls')

    setting_choices = read_json_return("settings", "choices")

    modset = grab_modset()

    log_message(-1, f"Modset was {modset}")

    if (setting_choices <= 0):
        raise Exception("Choice is 0 or lower, please change.")

    if (setting_choices >= 100):
        raise Exception("Choice is 100 or higher, for the sake of your CPU i'm cancelling this early.")

    for i in range(setting_choices):

        factions = return_faction_choices(modset)

        display_factions(factions[0], factions[1])

    log_message(-1, "\nFinished.\nEnjoy your choices!")

init()