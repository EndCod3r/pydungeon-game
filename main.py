import character
import player

import json
from random import randint

# Game Setup

with open("player.json", "r") as f:
    data = json.load(f)

if data.get("hasCharacter") == False:
    character.characterSelector()

selectedCharacter = character.getCharacter()


print(f"Welcome to PyDungeons!\nYou're playing as a {selectedCharacter}.")
input("Press enter to continue...\n")

while True:
    player.enemyEncounter()
