from file_operations import write_to_file
from modset_json import read_json_return

setting_debug_level = read_json_return("settings", "debug_level")

# open the file so we can append to it later
write_to_file("output", ["Open File"], "w+")

def log_message(debug_level, message):
    if (debug_level == -1 and setting_debug_level <= 10):
        print(f"{message}")
        write_to_file("output", [message], "a+")

    if (debug_level == 0 and setting_debug_level == debug_level):
        print(f"Information: {message}")

    if (debug_level >= 1 and setting_debug_level == debug_level):
        print(f"Data: {message}")