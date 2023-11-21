from random import randint
import json

import game
from enemy import spawnEnemy


def getAttributes():
    from character import getCharacter

    selectedCharacter = getCharacter()

    class Character:
        def __init__(self, health, damage, speed, stealth):
            self.health = health  # Max 150
            self.damage = damage  # Max 100
            self.speed = speed  # Max 100
            self.stealth = stealth  # Max 50

    warrior_attributes = Character(100, 50, 25, 10)
    ninja_attributes = Character(80, 40, 50, 45)
    hunter_attributes = Character(75, 55, 35, 25)

    if selectedCharacter == "warrior":
        characterAttributes = warrior_attributes
    elif selectedCharacter == "ninja":
        characterAttributes = ninja_attributes
    elif selectedCharacter == "hunter":
        characterAttributes = hunter_attributes

    return characterAttributes


def encounterInput():
    while True:
        playerInput = input(
            "What do you want to do:\n1. Attack\n2. Flee\n3. Do nothing\nSelection: "
        )
        if playerInput == "1":
            playerInput = "Attack"
            break
        elif playerInput == "2":
            playerInput = "Flee"
            break
        elif playerInput == "3":
            playerInput = "Do nothing"
            break
        else:
            print("Invalid input! Try again.")
            playerInput = "Invalid"

    return playerInput


def increaseEnemyDefeated():
    with open("player.json", "r") as f:
        data = json.load(f)

    enemysDefeated = data.get("enemysDefeated")
    enemysDefeated = enemysDefeated + 1

    data["enemysDefeated"] = enemysDefeated

    with open("player.json", "w") as f:
        json.dump(data, f)


def enemyEncounter():
    enemyData = spawnEnemy()
    playerData = getAttributes()

    while True:
        didEnemyAttack = False
        playerInput = encounterInput()
        chanceToHit = randint(1, 3)
        chanceToFlee = randint(1, 4)
        chanceToWin = randint(1, 50)

        if playerInput == "Attack" and chanceToHit > 1:
            enemyData.health = enemyData.health - playerData.damage
            if enemyData.health <= 0:
                enemyData.health = 0

            print(f"You hit your attack! Enemy Health: {enemyData.health}")
            if enemyData.health <= 0:
                print("Enemy killed!")
                increaseEnemyDefeated()
                break
        elif playerInput == "Attack" and chanceToHit == 1:
            print("You missed your attack!")

        if (
            playerInput == "Flee"
            and chanceToFlee < 4
            and playerData.speed >= enemyData.speed
        ):
            print("You fleed!")
            break
        elif playerInput == "Flee" and chanceToFlee == 4:
            print("You tripped and was unable to flee!")

        if playerInput == "Do nothing" and chanceToWin == 1:
            print("You did nothing and the enemy died! Maybe from intimidation.")
            break
        elif playerInput == "Do nothing" and chanceToWin != 1:
            print("You did nothing!")

        if playerInput != "Invalid":
            # Enemy attack
            enemyFleeChance = randint(1, 5)
            enemyAttackChance = randint(1, 2)

            if enemyAttackChance == 1:
                didEnemyAttack = True

                if randint(1, 2) == 1:
                    enemyAttackDamage = enemyData.damage - enemyFleeChance
                else:
                    enemyAttackDamage = enemyData.damage + enemyFleeChance

                playerData.health = playerData.health - enemyAttackDamage
                print(
                    f"The {enemyData.enemy} hit you and did {enemyAttackDamage} damage!"
                )
                with open("player.json", "r") as f:
                    data = json.load(f)

                data["currentHealth"] = playerData.health

                with open("player.json", "w") as f:
                    json.dump(data, f)

                if playerData.health <= 0:
                    print("You have died! Reseting game.")
                    game.resetGame()
                    quit()
                else:
                    print(f"You are now at {playerData.health}")
            else:
                print("The enemy attacked and missed!")

            if enemyFleeChance == 5 and didEnemyAttack == False:
                print("Enemy has fleed!")
                break
            else:
                continue
