# antistasi_modset_generator
 
The actual script you need to run is "modset_data.py". Settings are located in "json\settings.json"

# settings.json
```
{
    "modsets": "random_multiple",
    "desired_climate": ["temperate"],
    "desired_era": "modern",
    "desired_key": "vanilla",
    "desired_dlc": ["none"],
    "allow_double_occ": 0,
    "choices": 5,
    "debug_level": 0
}
```

## "modsets" 
Can be an array of modsets (in modsets.json). For example, ["rhs", "3cbf", "3cbbaf"]

If set to "random" it will choose 1 modset out of all the modsets.

If set to "random_multiple" it will choose random factions from all available modsets.

## "desired_climate"
Can be an array of climates or a singular string climate. For example ["arid", "temperate"] will return any factions matching either climate. "arid" will just return factions matching arid.

If set to "all_climates" it will use all 4 standard climates.

## "desired_era"
Has to be a string. Currently "modern" is the only era.

## "desired_key"
Has to be a string. Currently the only keys are "vanilla" and "rhs"

## "desired_dlc"
Has to be an array. If "none" is in the array, it will include every faction that requires no dlc (RHS and Vanilla, for example). 

If "ws" is in the array, it will include every faction that requires ws (Aegis and WS factions for example).

## "allow_double_occ"
Has to be 0 or 1. If set to 1, the invader and occupier pools are merged.

## "choices"
The amount of choices you want. Has to be an int. Please don't set this to 0 or lower, I didn't bother adding an exception for it.

## "debug_level"
The amount of debug messages you'll get. You usually don't need to change this, but anything higher than 2 will give you a huge amount of information.