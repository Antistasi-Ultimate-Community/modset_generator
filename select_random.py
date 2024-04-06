import random
import modset_factions

from modset_json import read_json_return
from logging import log_message

def select_random(array):
    data = array[random.randrange(0, len(array))]

    return data

def select_random_factions(modset):

    faction_classes = modset_factions.start_search(modset)

    faction_classes_occ = faction_classes[1][modset_factions.modset_faction_index_Occ]
    faction_classes_inv = faction_classes[1][modset_factions.modset_faction_index_Inv]
    faction_classes_reb = faction_classes[1][modset_factions.modset_faction_index_Reb]
    faction_classes_riv = faction_classes[1][modset_factions.modset_faction_index_Riv]
    faction_classes_civ = faction_classes[1][modset_factions.modset_faction_index_Civ]
    faction_collections = faction_classes[1][5]

    if (faction_classes_inv == []):
        faction_classes_inv = [["N/A"]]

    if (faction_classes_reb == []):
        faction_classes_reb = [["N/A"]]

    if (faction_classes_riv == []):
        faction_classes_riv = [["N/A"]]

    if (faction_classes_civ == []):
        faction_classes_civ = [["N/A"]]

    factions = [faction_classes_occ, faction_classes_inv, faction_classes_reb, faction_classes_riv, faction_classes_civ]

    setting_allow_double_occ = read_json_return("settings", "allow_double_occ")

    random_faction_occ = select_random(faction_classes_occ)
    if (setting_allow_double_occ):
        random_faction_occ = select_random(faction_classes_occ + faction_classes_inv)
        random_faction_inv = select_random(faction_classes_occ)
    else:
        random_faction_inv = select_random(faction_classes_inv)
    random_faction_reb = select_random(faction_classes_reb)
    random_faction_riv = select_random(faction_classes_riv)
    random_faction_civ = select_random(faction_classes_civ)

    log_message(3, [random_faction_occ, random_faction_inv, random_faction_reb, random_faction_riv, random_faction_civ])

    message = f"\nYour Occupier is the {random_faction_occ[0]}.\nyou are being invaded by the {random_faction_inv[0]}.\nYou'll be playing as the {random_faction_reb[0]} with your rivals being the {random_faction_riv[0]}.\nLocal civilians are {random_faction_civ[0]}."

    return [message, faction_collections]

def select_random_factions_multiple(modset, amount):
    modsets = []
    for i in range(amount):
        return_var = select_random_factions(modset)
        message = return_var[0].split(",")
        collections = return_var[1]
        modsets.extend([i, message])
    
    return [message, collections, modsets]