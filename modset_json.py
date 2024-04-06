import json
import os

def save_json(data, file_name):

    with open(f'{os.getcwd()}/json/{file_name}.json', 'w+') as file:
        json.dump(data, file, indent=4)

def read_json(file_name):
    with open(f'{os.getcwd()}/json/{file_name}.json', 'r') as file:
        y = json.load(file)

    return y

def read_json_return(file_name, data):
    if ("/" in file_name):
        
        with open(f'json/{file_name}', 'r') as file:
            x = json.load(file)

    else:

        with open(f'{os.getcwd()}/json/{file_name}.json', 'r') as file:
            x = json.load(file)

    if (data not in x):
        x.update({data: ""})

    y = x[data]

    return y

def update_json(data, file_name):

    print(data)

    try:

        with open(f'{os.getcwd()}/json/{file_name}.json', 'r') as file:
            y = json.load(file)

        y.update(data)

        save_json(y, file_name)

    except:
        print("Woops!")
        # prompt.user_error("Error", "Something went wrong whilst saving settings. Some things may still work. Try creating an empty packer.json file")