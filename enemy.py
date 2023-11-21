def selectEnemy():
    from random import randint

    enemy = randint(1, 3)
    if enemy == 1:
        selectedEnemy = "Goblin"
    elif enemy == 2:
        selectedEnemy = "Skeleton"
    elif enemy == 3:
        selectedEnemy = "Zombie"
    return selectedEnemy


def setAttributes(selectedEnemy):
    class Enemy:
        def __init__(self, enemy, health, damage, speed):
            self.enemy = enemy
            self.health = health  # Max 50
            self.damage = damage  # Max 50
            self.speed = speed  # Max 50

    if selectedEnemy == "Goblin":
        enemyAttributes = Enemy("Goblin", 25, 10, 20)
    elif selectedEnemy == "Skeleton":
        enemyAttributes = Enemy("Skeleton", 15, 20, 25)
    elif selectedEnemy == "Zombie":
        enemyAttributes = Enemy("Zombie", 15, 25, 15)
    return enemyAttributes


def spawnEnemy():
    selectedEnemy = selectEnemy()
    enemyData = setAttributes(selectedEnemy)
    print(
        f"You encountered a {enemyData.enemy}\nHealth: {enemyData.health}\nDamage: {enemyData.damage}\nSpeed: {enemyData.speed}"
    )
    return enemyData
