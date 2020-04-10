from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to the rooms

room['outside'].add_item(Item('Sword', 'It\'s a sword yo'))
room['outside'].add_item(Item('Rock', 'What do you want me to say?'))
room['foyer'].add_item(Item('Map', 'It\'s a map'))
room['overlook'].add_item(Item('Key', 'It unlocks stuff and things'))
room['narrow'].add_item(Item('Potion', 'It uhm does, magic'))
room['treasure'].add_item(Item('Duck', 'It\'s a rubber duck yo'))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

class colors:
    blink = '\033[5m'
    red = '\033[91m'
    yellow = '\033[93m'
    reset = '\033[0m'

def playerInfo():
    print(f'\n{colors.yellow}{player.name} is currently located in the {player.current_room.name}.\n')
    print(f'{player.current_room.description}\n{colors.reset}')

def invalidSelection(sentence = 'You cannot got that way.'):
    print(f'{colors.red}{colors.blink}\n{sentence}{colors.reset}')

def itemsInPlayerRoom():
    print('Items in the room:')
    for item in player.current_room.items:
        print(f'{colors.yellow}{item.name}: {item.description}{colors.reset}')

def commands():
    print('\nPlease choose a command...')
    return input("[n] North [w] West [e] East [s] South [Get Item] [Drop Item] [i] Inventory [q] Quit\n")
    

playerName = input('Choose a name: ')
player = Player(playerName, room['outside'])
playerInfo()
itemsInPlayerRoom()
command = commands()
splitCommand = command.split(' ')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while not command == 'q':    
    
    splitCommand = command.split(' ')

    if len(splitCommand) == 1:
        if command == 'n':
            if player.current_room.n_to == None:
                invalidSelection()
            else: 
                player.update_room(player.current_room.n_to)
        elif command == "s":
            if player.current_room.s_to == None:
                invalidSelection()
            else:
                player.update_room(player.current_room.s_to)
        elif command == "w":
            if player.current_room.w_to == None:
                invalidSelection()
            else:
                player.update_room(player.current_room.w_to)
        elif command == "e":
            if player.current_room.e_to == None:
                invalidSelection()
            else:
                player.update_room(player.current_room.e_to)
        elif command == 'i' or 'inventory':
            player.get_inventory()
        else:
            invalidSelection('Try again, pick a valid direction this time.')
    elif len(splitCommand) == 2:

        if splitCommand[0].lower() == 'get':
            for item in player.current_room.items:
                if item.name.lower() == splitCommand[1].lower():
                    player.current_room.items.remove(item)
                    player.inventory.append(item)
                    item.on_take(item.name.lower())
        
        elif splitCommand[0].lower() == 'drop':
            for item in player.inventory:
                if item.name.lower() == splitCommand[1].lower():
                    player.inventory.remove(item)
                    player.current_room.items.append(item)
                    item.on_drop(item.name.lower())
        else:
            print('That command doesn\'t exist.')
    else:
        print('That command doesn\'t exist.')


    playerInfo()
    itemsInPlayerRoom()

    command = commands()

    # print('\nPlease choose a direction to continue...')
    # commands = input("[n] North [w] West [e] East [s] South [q] Quit\n")
    