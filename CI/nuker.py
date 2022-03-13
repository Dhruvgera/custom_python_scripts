import json,glob,os

device_name = "device_name_here"

path_to_dep = glob.glob(f"device/*/{device_name}/cygnus.dependencies")[0]

def nuke():
    with open(path_to_dep) as file:
        json_data = json.loads(file.read())
        for repos in json_data:
            os.system(f"rm -rf {repos['target_path']}")

nuke()
