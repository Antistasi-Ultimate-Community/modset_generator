from modset_json import read_json_return
import os
import random

from logging import log_message

# Common vars
faction_file = "factions"

required_collections = [];
factions_occ = []
factions_inv = []
factions_reb = []
factions_riv = []
factions_civ = []

setting_desired_climate = read_json_return("settings", "desired_climate")
setting_desired_era = read_json_return("settings", "desired_era")
setting_desired_key = read_json_return("settings", "desired_key")
setting_key_exclusive = read_json_return("settings", "key_exclusive")

def validate_faction_era(faction_era):
    if (isinstance(setting_desired_era, list)):
        for era in setting_desired_era:
            if (faction_era == era):
                return True

        return False

    if (faction_era == setting_desired_era):
        return True
    else:
        return False

def validate_faction_climate(faction_climate):
    log_message(3, faction_climate)
    if (isinstance(setting_desired_climate, list)):
        for climate in setting_desired_climate:
            log_message(3, climate)
            if (climate in faction_climate):
                return True

        return False

    if (setting_desired_climate in faction_climate):
        return True
    else:
        return False

def validate_factions_data(factions_data):
    log_message(3, factions_data)

def grab_factions_data_multiple(factions, modset, faction_type):
        
    for faction in factions:

        faction_data_side = grab_faction_object(modset=modset, faction_type=faction_type, data="side")
        faction_data_collection = grab_faction_object(modset=modset, data="collection").split(",")
        faction_data_era = grab_faction_object(modset=modset, data="era")
        faction_data_type = grab_faction_object(modset=modset, data="type")
        faction_data_title = grab_faction_object(modset=modset, faction_type=faction_type, faction=faction, data="title").split(",")
        faction_data_climates = grab_faction_object(modset=modset, faction_type=faction_type, faction=faction, data="climates")
        
        if (faction_data_collection not in required_collections):
            required_collections.append(faction_data_collection)

        if (setting_key_exclusive and faction_data_type != setting_desired_key):
            continue

        climate_verify = validate_faction_climate(faction_data_climates)
        log_message(3, climate_verify)
        if (climate_verify == False):
            continue

        era_verify = validate_faction_era(faction_data_era)
        log_message(3, era_verify)
        if (era_verify == False):
            break

        new_data = [faction_data_title[0], faction_data_climates, faction_data_type, faction_data_side]

        if (faction_data_side == "Occ"):
            factions_occ.append(new_data)

        if (faction_data_side == "Inv"):
            factions_inv.append(new_data)

        if (faction_data_side == "Reb"):
            factions_reb.append(new_data)

        if (faction_data_side == "Riv"):
            factions_riv.append(new_data)

        if (faction_data_side == "Civ"):
            factions_civ.append(new_data)

    factions_data = [factions_occ, factions_inv, factions_reb, factions_riv, factions_civ, required_collections]

    validate_factions_data(factions_data)

    return factions_data

def grab_factions_data(factions, modset):
    faction_classes = []
    for faction in factions:
        faction_type = faction[0]
        faction_class = faction[1]

        if (len(faction) > 1):
            for faction in faction:
                if (len(faction[0]) != 1):
                    faction_classes.extend(faction)
            
                    factions_all = grab_factions_data_multiple(faction, modset, faction_type)

    return [faction_classes, factions_all]

def grab_faction_object(modset, faction_type="", faction="", data=""):
    faction_data = grab_faction(faction_file)
    faction_data_return = ""

    # deal with it, can't be bothered making a proper method
    if (faction_type == "" and faction == "" and modset != "" and data != ""):
        faction_data_return = faction_data[0][modset][data]

    if (faction == "" and data == "" and faction_data_return == ""):
        faction_data_return = faction_data[0][modset][faction_type]

    if (faction == "" and faction_type != "" and faction_data_return == ""):
        faction_data_return = faction_data[0][modset][faction_type][data]

    if (data == "" and faction_type != "" and faction_data_return == ""):
        faction_data_return = faction_data[0][modset][faction_type][faction]

    if (modset != "" and faction_type != "" and faction != "" and data != ""):
        faction_data_return = faction_data[0][modset][faction_type][faction][data]


    return faction_data_return

def grab_faction(faction):
    faction_data = read_json_return(faction, faction)

    return faction_data

# grab_faction_object(modset="rhs", faction_type="factionsOcc", faction="RHS_USMC_Arid", data="dlc")