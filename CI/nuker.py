import json,glob

device_name = "device_name_here"

path_to_dep = glob.glob(f"device/*/{device_name}/cygnus.dependencies")[0]

def nuke():
    with open(path_to_dep) as file:
        json_data = json.loads(file.read())
        for repos in json_data:
            print(f"rm -rf {repos['target_path']}")

nuke()