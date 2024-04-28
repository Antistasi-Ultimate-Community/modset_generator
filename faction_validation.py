from common_vars import *

def validate_faction_dlc(faction_dlc):
    if (isinstance(setting_desired_dlc, list)):
        for dlc in faction_dlc:
            if (dlc in setting_desired_dlc):
                return True

        return False

    if (faction_dlc == setting_desired_dlc):
        return True
    else:
        return False

def validate_faction_era(faction_era):
    if (faction_era in setting_desired_era):
        return True
    else:
        return False

def validate_faction_key(faction_key):
    if (faction_key == ""):
        return True

    if (faction_key == setting_desired_key):
        return True
    else:
        return False

def validate_faction_climate(faction_climate):

    if (isinstance(setting_desired_climate, list)):
        for climate in setting_desired_climate:
            if (climate in faction_climate):
                return True

        return False

    if (setting_desired_climate in faction_climate):
        return True
    else:
        return False

def validate_faction(faction_climates, faction_era, faction_key, faction_dlc):

    validation_climate = validate_faction_climate(faction_climates)
    validation_era = validate_faction_era(faction_era)
    validation_key = validate_faction_key(faction_key)
    validation_dlc = validate_faction_dlc(faction_dlc)

    if (validation_climate == False or validation_dlc == False or validation_era == False or validation_key == False):
    
        return False

    return True

def validate_faction_data(faction_dict, modset_dict):

    for faction_type in faction_types:

        factions = list(faction_dict[faction_type].keys())

        for faction in factions:

            faction_climates = faction_dict[faction_type][faction]["climates"]
            faction_modset = faction_dict[faction_type][faction]["modset"]
            faction_dlc = faction_dict[faction_type][faction]["dlc"]

            faction_key = modset_dict[faction_modset]["type"]
            faction_era = modset_dict[faction_modset]["era"]
            
            validation = validate_faction(faction_climates, faction_era, faction_key, faction_dlc)

            if (validation == False):
                del faction_dict[faction_type][faction]