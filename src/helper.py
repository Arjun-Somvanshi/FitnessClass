import json 

def load_colors() -> dict:
    with open("res/colors.json", "r") as f:
        colors = json.load(f) 
    return colors
