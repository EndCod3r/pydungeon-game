import json
from player import getAttributes


def writeCharacter(character):
    with open("player.json", "r") as f:
        data = json.load(f)

    data["hasCharacter"] = True
    data["character"] = character
    data["level"] = 1

    with open("player.json", "w") as f:
        json.dump(data, f)

    characterHealth = getAttributes()
    characterHealth = characterHealth.health

    data["currentHealth"] = characterHealth

    with open("player.json", "w") as f:
        json.dump(data, f)


def characterSelector():
    print("1. Warrior\n2. Ninja\n3. Hunter")
    character_selection = input("Which character would you like to use?: ").lower()

    if character_selection == "1":
        character_selection = "warrior"
    elif character_selection == "2":
        character_selection = "ninja"
    elif character_selection == "3":
        character_selection = "hunter"

    if (
        character_selection == "warrior"
        or character_selection == "ninja"
        or character_selection == "hunter"
    ):
        writeCharacter(character_selection)
    else:
        print("Invalid input! Try again.")


def getCharacter():
    with open("player.json", "r") as f:
        data = json.load(f)
    return data.get("character")
