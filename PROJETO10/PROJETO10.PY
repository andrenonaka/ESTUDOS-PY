import random
import sys
import tkinter as tk
from tkinter import ttk
from typing import List

#item class and list
class items:
    def __init__(self, item_name, item_description, item_amount):
        self.item_name = item_name
        self.item_description = item_description
        self.item_amount = item_amount

arrow = items('Arrow', 'Used to stab from afar.', 1)
sword = items('Sword', 'Used to stab when close', 0)
poison = items('Poison Vial', 'Kills without stabbing', 0)
book = items('Magic Book', 'Used to stab dragons.', 0)
item_list = [arrow, sword, poison, book]

#monster class and list

class monsters:
    def __init__(self, monster_name, monster_description, monster_weakness, monster_attack_fail_msg):
        self.monster_name = monster_name
        self.monster_description = monster_description
        self.monster_weakness = monster_weakness
        self.monster_attack_fail_msg = monster_attack_fail_msg

goblin = monsters('Goblin', 'A green, small monster.', 'Arrow', 'Attack failed')
harpy = monsters('Harpy', 'A feathered horror of the skies.', 'Sword', 'Attack failed')
witch = monsters('Witch', 'A hag that carries powerful magics.', 'Poison Vial', 'Attack failed')
dragon = monsters('Dragon', 'A god-like, gold-seeking creature.', 'Magic Book', 'Attack failed')
monster_list: List[monsters] = [goblin, harpy, witch, dragon]
monster_name_dict = {monster.monster_name: monster for monster in monster_list} #ESTUDAR <<<<<<<<<<<<<<<
monster_name_list = [name.monster_name for name in monster_list]
#study list comprehension.
#list comprehension is a way to iterate on lists for each item of that list using a single expression.
#syntax: new_list = ["new item" for "item" in "oldlist"]
#"new item" is what is being put in the new list. "new item" can be just an item or an expression.
#example of use: I have a list of numbers. I want to create a new list with the same numbers but add 1 to all of them.
#new_number_list = [number+1 for number in old_number_list]
#in the case of a list which contains class objects, such as monster_list above, we
#want to extract only one of the parameters (in this case, .monster_name) from that object to put in the new list.
#So, the syntax should be something like: list_of_parameters = [object.object_parameter for object in object_list]

#window
window = tk.Tk()
window.title('Projeto10')
window.geometry('800x300')

#notebook
notebook = ttk.Notebook(master = window)
notebook.pack(fill = 'both', expand = True)

#main tab
main_tab = ttk.Frame(notebook)
main_label_tab = ttk.Label(master = main_tab, text = 'Label')
main_label_tab.pack(anchor = 'w')

#inventory
inventory_tab = ttk.Frame(master = notebook)

tree_frame = ttk.Frame(master = inventory_tab, padding = 30)
tree_frame.pack()

inventory_tree = ttk.Treeview(master = tree_frame, columns = ('name', 'description', 'amount'), show = 'headings')
inventory_tree.heading('name', text = 'Name')
inventory_tree.heading('description', text = 'Description')
inventory_tree.heading('amount', text = 'Amount')
inventory_tree.pack(side = 'left')
for item in item_list:
    inventory_tree.insert(parent = '', index = 'end', values = (item.item_name, item.item_description, item.item_amount))
    

tree_scroll = ttk.Scrollbar(master = tree_frame, orient = 'vertical', command = inventory_tree.yview)
tree_scroll.pack(side = 'right', fill = 'y')
inventory_tree.configure(yscrollcommand = tree_scroll.set)

#monster menu
monster_tab = ttk.Frame(master = notebook)
monster_tab.pack()

monster_dropbox = ttk.Combobox(master = monster_tab, values = monster_name_list)
monster_dropbox.pack(anchor = 'nw', pady = '10')

monster_name_label_var = tk.StringVar()
monster_name_label = ttk.Label(master = monster_tab, textvariable = monster_name_label_var)
monster_name_label.pack(anchor = 'w')

monster_description_label_var = tk.StringVar()
monster_description_label = ttk.Label(master = monster_tab, textvariable = monster_description_label_var)
monster_description_label.pack(anchor = 'w')

def monster_label_updates(name_label_var, description_label_var, value, event = None): #event functions must receive the event as well for some reason
    dropbox_value = value.get()
    # name_label_var.set(dropbox_value)
    monster = monster_name_dict[dropbox_value]
    description_label_var.set(monster.monster_description)
    name_label_var.set(monster.monster_name)
    
monster_dropbox.bind("<<ComboboxSelected>>", lambda event: monster_label_updates(monster_name_label_var, monster_description_label_var, monster_dropbox, event))

# def monster_attack(monster_chosen, monster_list):
#     for name in monster_list:
#         if name == monster_chosen.monster_name:

# attack_button = ttk.Button(master = monster_tab, command = lambda: monster_attack())
# attack_button.pack(anchor = 'w')

notebook.add(main_tab, text = "Main Menu")
notebook.add(inventory_tab, text = "Inventory")
notebook.add(monster_tab, text = "Monsters")

window.mainloop()

# def main_menu():
#     print('Main Menu')
#     print('type a number to choose, or type nothing to quit')
#     print('0 - show inventory')
#     print('1 - attack monster')
#     while True:
#         command = input()
#         if command == '':
#             sys.exit()
#         elif int(command) == 0: #input 0 = show inventory
#             manage_inv()
#         elif int(command) == 1: #input 1 = choose monster to attack
#             choose_attack()

# def manage_inv():
#     while True:
#         print('Current inventory. Type nothing to return to main menu.')
#         print(inventory)
#         command = input()
#         if command == '':
#             main_menu()
    
# def choose_attack():
#     print('Choose a monster to attack or type nothing to return to main menu.')
#     print(monsters)
#     choiceAtk = input()
#     if choiceAtk == '':
#         main_menu()
#     if choiceAtk not in monsters:
#         print('There is no such monster. Choose another.')
#         choose_attack()
#     elif choiceAtk == 'goblin':
#         atk_goblin()
#     elif choiceAtk == 'harpy':
#         atk_harpy()
#     elif choiceAtk == 'witch':
#         atk_witch()
#     elif choiceAtk == 'dragon':
#         atk_dragon()

# def atk_goblin():
#     if inventory['arrow'] > 0:
#         inventory['arrow'] -= 1
#         print('You defeated the greasy goblin! And you found some loot!')
#         arrowGet = random.randint(1, 2)
#         if arrowGet > 0:
#             print('You got ' + str(arrowGet) + 'arrow(s)!')
#             inventory['arrow'] += arrowGet
#         swordGet = random.randint(0, 1)
#         if swordGet > 0:
#             print('You got ' + str(swordGet) + 'sword(s)!')
#             inventory['sword'] += swordGet
#         choose_attack()
#     else:
#         print('This monster requires an arrow to defeat and you have none. Choose another monster.')
#         choose_attack()

# def atk_harpy():
#     if inventory['sword'] > 0:
#         inventory['sword'] -= 1
#         print('You defeated the horrible harpy! And you found some loot!')
#         swordGet = random.randint(1, 2)
#         if swordGet > 0:
#             print('You got ' + str(swordGet) + 'sword(s)!')
#             inventory['sword'] += swordGet
#         poisonGet = random.randint(0, 1)
#         if poisonGet > 0:
#             print('You got ' + str(poisonGet) + 'vial(s) of poison!')
#             inventory['poison vial'] += poisonGet
#         choose_attack()
#     else:
#         print('This monster requires a sword to defeat and you have none. Goblins sometimes carry swords. Choose another monster.')
#         choose_attack()

# def atk_witch():
#     if inventory['poison vial'] > 0:
#         inventory['poison vial'] -= 1
#         print('You defeated the wonderous witch! And you found some loot!')
#         poisonGet = random.randint(1, 2)
#         if poisonGet > 0:
#             print('You got ' + str(poisonGet) + 'vial(s) of poison')
#             inventory['poison vial'] += poisonGet
#         bookGet = random.randint(0, 1)
#         if bookGet > 0:
#             print('You got ' + str(bookGet) + 'magic book(s)')
#             inventory['magic book'] += bookGet
#         choose_attack()
#     else:
#         print('This monster requires a poison vial to defeat and you have none. Harpies sometimes carry poison vials. Choose another monster.')
#         choose_attack()

# def atk_dragon():
#     if inventory['magic book'] > 0:
#         inventory['magic book'] -= 1
#         print('You defeated the demonic dragon!')
#         crownGet = random.randint(0, 1)
#         if crownGet > 0:
#             print('You got the Royal Crown! Congratulations! You saved the land!')
#             print('Your deeds will be remembered. Thank you for playing!')
#             sys.exit()
#         else:
#             print('Unfortunately, this dragon was not carrying the Royal Crown. Try gain!')       
#             choose_attack()
#     else:
#         print('This monster requires a magic book to defeat and you have none. Witches sometimes carry magic books. Choose another monster.')
#         choose_attack()

# # print('Welcome, adventurer! The kingdom is in peril!')
# # print("The Dragon Clan stole the Royal Crown! One of the Dragons now carries our kingdom's treasure!")
# # print('Please help us! Defeat the dragons and find the Royal Crown!')
# # print('')
# # main_menu()