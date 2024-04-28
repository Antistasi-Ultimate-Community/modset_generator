from file_operations import write_to_file
from modset_json import read_json_return

from common_vars import setting_debug_level

# open the file so we can append to it later
write_to_file("output", ["Open File"], "w+")

def log_message(debug_level, message):
    if (debug_level == -1 and setting_debug_level <= 10):
        print(f"{message}")
        write_to_file("output", [message], "a+")

    if (debug_level == 0 and setting_debug_level == debug_level):
        print(f"\nInformation: {message}")

    if (debug_level >= 1 and setting_debug_level == debug_level):
        print(f"\nData: {message}")