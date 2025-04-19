## VIDEOGAME INVENTORY MANAGEMENT

Our objective is to create a videogame-like program were the player is tasked with retrieving a specific rare item from a specific monster.

The player is given an inventory with limited resources and a list of monsters to defeat. Each monster requires a specific item or items to be defeated. Each time the player defeats a monster, items will drop from those monsters based on random chance and will be added to that player's inventory. The item required to defead a subsequent monster has a random (not guaranteed) chance of dropping from the previous monster. The item required to kill a monster will always drop from that same monster.

We will be using dictionaries to manage the player's inventory. Since a dictionary cannot have identical keys, we will be using the keys as the item designation and the values as the item amount, such as this: inventory = {'item1':amount, 'item2':amount ...}.

```python
inventory = {'arrow': 1, 'sword': 0, 'poison vial':0, 'magic book':0}
```

The monsters will be managed by using a list. We could also use dictionaries for the monters, maybe the monster name as the key and nest another dictionary inside the key to indicate the possible item drops and other things, but it is not necessary for the purposes of this exercise and we wanted to mix the use of dictionaries and lists in a single program for study purposes.

```python
monsters = ['goblin', 'harpy', 'witch', 'dragon']
```
We will have a main menu that will allow the player to see the inventory and choose the monter menu. Note that the menu does not have any safeguards against the player typing a number that doesn't correspond to any option in the menu. We did this purposefully to check if the program would break in such situation, and it does not. The "while True" line simply does nothing if the user types something that isn't in the menu, and keeps checking for valid inputs. Because of this, we do not need to recall the menu function every time the user types something that is not a valid input.

```python
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
```
The inventory menu simply prints the inventory dictionary. "while True" is used to avoid invalid inputs by the user.

```python
def manage_inv():
    print('Current inventory. Type nothing to return to main menu.')
    print(inventory)
    command = input()
    while True:
        if command == '':
            main_menu()
```

Monster attacks are dictated by very similar functions such as the one below. We check if the user has the required item in their inventory to defeat the monster and, if so, they defeat the monster and receive loot. As stated before, the player will always receive at least one of the item necessary to defeat that same monster (this makes the game literally impossible to lose) and has a chance (not guarantee) to receive the item necessary to defeat the next monster.

```python
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
```
Note that the message indicating that the goblin requires arrows to beat will never appear in normal circunstances, since the player starts with one arrow and aways receives an arrow upon defeating a goblin. However, we may want to get back to this project in the future to add further features (such as making it possible for the player to lose all arrows and needing to find additional arrows in some other way), so we included this even though it is redundant for now.

The game ends when the player successfully loots the Royal Crown from the Dragon. We import sys to make it possible to end the program when this happens:

```python
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
```


