import random
import sys

inventory = {'arrow': 1, 'sword': 0, 'poison vial':0, 'magic book':0}
monsters = ['goblin', 'harpy', 'witch', 'dragon']

def main_menu():
    print('Main Menu')
    print('type a number to choose, or type nothing to quit')
    print('0 - show inventory')
    print('1 - attack monster')
    while True:
        command = input()
        if command == '':
            sys.exit()
        elif int(command) == 0: #input 0 = show inventory
            manage_inv()
        elif int(command) == 1: #input 1 = choose monster to attack
            choose_attack()

def manage_inv():
    print('Current inventory. Type nothing to return to main menu.')
    print(inventory)
    command = input()
    while True:
        if command == '':
            main_menu()
    
def choose_attack():
    print('Choose a monster to attack or type nothing to return to main menu.')
    print(monsters)
    choiceAtk = input()
    if choiceAtk == '':
        main_menu()
    if choiceAtk not in monsters:
        print('There is no such monster. Choose another.')
        choose_attack()
    elif choiceAtk == 'goblin':
        atk_goblin()
    elif choiceAtk == 'harpy':
        atk_harpy()
    elif choiceAtk == 'witch':
        atk_witch()
    elif choiceAtk == 'dragon':
        atk_dragon()

def atk_goblin():
    if inventory['arrow'] > 0:
        inventory['arrow'] -= 1
        print('You defeated the greasy goblin! And you found some loot!')
        arrowGet = random.randint(1, 2)
        if arrowGet > 0:
            print('You got ' + str(arrowGet) + 'arrow(s)!')
            inventory['arrow'] += arrowGet
        swordGet = random.randint(0, 1)
        if swordGet > 0:
            print('You got ' + str(swordGet) + 'sword(s)!')
            inventory['sword'] += swordGet
        choose_attack()
    else:
        print('This monster requires an arrow to defeat and you have none. Choose another monster.')
        choose_attack()

def atk_harpy():
    if inventory['sword'] > 0:
        inventory['sword'] -= 1
        print('You defeated the horrible harpy! And you found some loot!')
        swordGet = random.randint(1, 2)
        if swordGet > 0:
            print('You got ' + str(swordGet) + 'sword(s)!')
            inventory['sword'] += swordGet
        poisonGet = random.randint(0, 1)
        if poisonGet > 0:
            print('You got ' + str(poisonGet) + 'vial(s) of poison!')
            inventory['poison vial'] += poisonGet
        choose_attack()
    else:
        print('This monster requires a sword to defeat and you have none. Goblins sometimes carry swords. Choose another monster.')
        choose_attack()

def atk_witch():
    if inventory['poison vial'] > 0:
        inventory['poison vial'] -= 1
        print('You defeated the wonderous witch! And you found some loot!')
        poisonGet = random.randint(1, 2)
        if poisonGet > 0:
            print('You got ' + str(poisonGet) + 'vial(s) of poison')
            inventory['poison vial'] += poisonGet
        bookGet = random.randint(0, 1)
        if bookGet > 0:
            print('You got ' + str(bookGet) + 'magic book(s)')
            inventory['magic book'] += bookGet
        choose_attack()
    else:
        print('This monster requires a poison vial to defeat and you have none. Harpies sometimes carry poison vials. Choose another monster.')
        choose_attack()

def atk_dragon():
    if inventory['magic book'] > 0:
        inventory['magic book'] -= 1
        print('You defeated the demonic dragon!')
        crownGet = random.randint(0, 1)
        if crownGet > 0:
            print('You got the Royal Crown! Congratulations! You saved the land!')
            print('Your deeds will be remembered. Thank you for playing!')
            sys.exit()
        else:
            print('Unfortunately, this dragon was not carrying the Royal Crown. Try gain!')       
            choose_attack()
    else:
        print('This monster requires a magic book to defeat and you have none. Witches sometimes carry magic books. Choose another monster.')
        choose_attack()

print('Welcome, adventurer! The kingdom is in peril!')
print("The Dragon Clan stole the Royal Crown! One of the Dragons now carries our kingdom's treasure!")
print('Please help us! Defeat the dragons and find the Royal Crown!')
print('')
main_menu()