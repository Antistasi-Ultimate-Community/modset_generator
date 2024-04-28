# antistasi_modset_generator
 
The actual file you need to run is "init.py". Settings are located in "json\settings.json"

# settings.json
```
{
    "modsets": "random_multiple",
    "desired_climate": ["temperate"],
    "desired_era": "modern",
    "desired_key": "rhs",
    "desired_dlc": ["none"],
    "allow_double_occ": 0,
    "choices": 1,
    "debug_level": 0,
    "force_faction_occ": [],
    "force_faction_inv": [],
    "force_faction_reb": [],
    "force_faction_riv": [],
    "force_faction_civ": []
}
```

The example above will return 1 choice of RHS based factions that match the temperate climate, are modern, and don't have any DLC.

```
Choice 1
Your Occupier is the TFC Canadian Army (Temperate).
you are being invaded by the RHS SAF.
You'll be playing as the 3CB CCM with your rivals being the 3CB CHDKZ.
Local civilians are RHS Eastern Europeans.
```

## "modsets" 
Can be an array of modsets (in modsets.json). For example, `["rhs", "3cbf", "3cbbaf"]`

~~If set to "random" it will choose 1 modset out of all the modsets.~~
This has been deprecated in favour of below.

If set to `"random_multiple"` it will choose random factions from all available modsets.

## "desired_climate"
Can be an array of climates or a singular string climate. For example `["arid", "temperate"]` will return any factions matching either climate. `"arid"` will just return factions matching arid.

If set to `"all_climates"` it will use all 4 standard climates.

## "desired_era"
Has to be a string. Current eras are: `["modern", "scifi", "lowtech", "coldwar"]`

## "desired_key"
Has to be a string. Current keys are: `["vanilla", "rhs"]`

## "desired_dlc"
Has to be an array. If `"none"` is in the array, it will include every faction that requires no dlc (RHS and CUP, for example).

If `"ws"` is in the array, it will include every faction that requires Western Sahara (Aegis and WS factions for example).

Current dlcs are: `["vanilla", "ws", "gm", "vn", "none"]`

## "allow_double_occ"
Has to be 0 or 1. If set to 1, the invader and occupier pools are merged.

## "choices"
The amount of choices you want. Has to be an int.

## "debug_level"
The amount of debug messages you'll get. You usually don't need to change this, but anything higher than 0 will give you debug information.

## "force_faction_x"
Has to be an array in format `["faction_type", "faction"]`. This ignores all the other "desired" settings.

For example, if you want to force RHS AFRF as occupant it would be: 

`"force_faction_occ": ["factionsInv", "RHS_AFRF"]`

If set to `[]` it will not force any faction. This is the same for all of the below respectively.

### "force_faction_occ"

### "force_faction_inv"

### "force_faction_reb"

### "force_faction_riv"

### "force_faction_civ"
