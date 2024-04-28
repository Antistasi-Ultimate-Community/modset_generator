from modset_json import read_json_return

faction_types = ["factionsOcc", "factionsInv", "factionsReb", "factionsRiv", "factionsCiv"]

setting_desired_climate = read_json_return("settings", "desired_climate")

if (setting_desired_climate == "all_climates"):
    setting_desired_climate = ["arid", "temperate", "tropical", "arctic"]

setting_desired_era = read_json_return("settings", "desired_era")
setting_desired_key = read_json_return("settings", "desired_key")
setting_desired_dlc = read_json_return("settings", "desired_dlc")
setting_key_exclusive = read_json_return("settings", "key_exclusive")

setting_allow_double_occ = read_json_return("settings", "allow_double_occ")

setting_force_faction_occ = read_json_return("settings", "force_faction_occ")
setting_force_faction_inv = read_json_return("settings", "force_faction_inv")
setting_force_faction_reb = read_json_return("settings", "force_faction_reb")
setting_force_faction_riv = read_json_return("settings", "force_faction_riv")
setting_force_faction_civ = read_json_return("settings", "force_faction_civ")

setting_debug_level = read_json_return("settings", "debug_level")