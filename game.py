import json


def resetGame():
    with open("player.json", "r") as f:
        data = json.load(f)

    data["hasCharacter"] = False
    data["character"] = ""
    data["level"] = 0
    data["currentHealth"] = 0
    data["enemysDefeated"] = 0

    with open("player.json", "w") as f:
        json.dump(data, f)
