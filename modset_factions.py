from modset_json import read_json_return
import factions_data
import os
import random

from select_random import select_random

from logging import log_message

# Common vars
modset_faction_prefix_Occ = "factionsOcc"
modset_faction_prefix_Inv = "factionsInv"
modset_faction_prefix_Reb = "factionsReb"
modset_faction_prefix_Riv = "factionsRiv"
modset_faction_prefix_Civ = "factionsCiv"

modset_faction_index_Occ = 0
modset_faction_index_Inv = 1
modset_faction_index_Reb = 2
modset_faction_index_Riv = 3
modset_faction_index_Civ = 4

modset_factions = [
    modset_faction_prefix_Occ,
    modset_faction_prefix_Inv,
    modset_faction_prefix_Reb, 
    modset_faction_prefix_Riv, 
    modset_faction_prefix_Civ
]

modset_faction_file = "modsets"

rhs_detected = False

def faction_match_climate(desired_climate, sub_faction_climate, sub_faction, faction):
    if (isinstance(desired_climate, list)):
        for climate in desired_climate:
            if (climate in sub_faction_climate):
                return True
                exit()

        if (sub_faction in faction):
            log_message(2, f"Removing {sub_faction} due to it not being the desired climate array.")
            faction.remove(sub_faction)

    if (desired_climate not in sub_faction_climate and (sub_faction in faction)):
        log_message(2, f"Removing {sub_faction} due to it not being the desired climate.")
        faction.remove(sub_faction)

    log_message(3, faction)

def clean_factions(factions, rhs_only=False, desired_climate="", desired_era=""):

    if (desired_climate == "" or desired_era == ""):
        log_message(4, "clean_factions is being ran without correct params.")
        exit()

def start_search(modset):
    if (isinstance(modset, list)):
        for mod in modset:
            mod = mod.casefold()
            factions = read_faction(mod)
            log_message(4, f"new mod is {mod}")
            faction_classes = factions_data.grab_factions_data(factions, mod)
    else:
        factions = read_faction(modset)
        faction_classes = factions_data.grab_factions_data(factions, modset)

    return faction_classes

def search_return_data(modset, index_1, index_2):
    faction_classes = start_search(modset)
    
    return faction_classes[index_1][index_2]

def grab_random_modset(file, key, random_modset=False):
    modset = read_json_return(file, key)
    
    if (random_modset == "random"):
        modset = select_random(modset)

    return modset

def grab_faction_index(faction):
    faction_index = -1

    if (faction == modset_faction_prefix_Occ):
        faction_index = modset_faction_index_Occ

    if (faction == modset_faction_prefix_Inv):
        faction_index = modset_faction_index_Inv

    if (faction == modset_faction_prefix_Reb):
        faction_index = modset_faction_index_Reb
        
    if (faction == modset_faction_prefix_Riv):
        faction_index = modset_faction_index_Riv

    if (faction == modset_faction_prefix_Civ):
        faction_index = modset_faction_index_Civ

    return faction_index

def grab_faction_data(modset, modset_faction):
    faction = read_json_return(modset_faction_file, modset)[modset_faction]

    return faction

def read_faction_data(modset, array, factions):
    for modset_faction in array:
        faction = grab_faction_data(modset, modset_faction)
        if (faction[0] != "None"):
            factions.append([modset_faction, faction])
        else:
            continue

    return factions

def read_faction_data_multiple(modsets, array):
    for modset in modsets:
        for modset_faction in array:
            faction = grab_faction_data(modset, modset_faction)
            factions.append([modset_faction, faction])

    factions_new = [[modset_faction_prefix_Occ],[modset_faction_prefix_Inv],[modset_faction_prefix_Reb],[modset_faction_prefix_Riv],[modset_faction_prefix_Civ]]
    
    for faction in factions:
        faction_prefix = faction[0]
        faction_array = faction[1]

        faction_index = grab_faction_index(faction_prefix)

        if (faction_index != -1):
            factions_new[faction_index].insert(faction_index + 1, faction_array)

    return factions_new
        

def read_faction(modset, array=modset_factions):

    factions = []

    if (isinstance(modset, list)):
        log_message(4, "Modset was array")
        factions = read_faction_data_multiple(modset, array)
    else:
        factions = read_faction_data(modset, array, factions)

    return factions