import json
import pathlib



SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
FILE_PATH = SCRIPT_DIR / "sample.json"






class player_state:
    pass




class game_state:
    pass







with FILE_PATH.open("r") as f:
    data =json.load(f)


# print(json.dumps(data , indent= 4 ))


for key ,  vlaue in data.items():
    print(key , vlaue)

player= player_state()




setattr(player ,)

