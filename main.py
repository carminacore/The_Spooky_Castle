from room import Room
from character import Enemy
from character import Friend
from rpginfo import RPGInfo
from item import Item

#Creates a new Room object without attributes
#Then the object is assigned to a variable
kitchen = Room('Kitchen')
dining_hall = Room('Dining hall')
ballroom = Room('Ballroom')

#Setting attributes descriptions
kitchen.description = 'A dark, dank and dirty place, buzzing with flies'
dining_hall.description = 'A large room with ornate golden decorations on each wall'
ballroom.description = 'A vast room with a shiny wooden floor'

#Setting attributtes linked rooms
kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

#Creating and setting the enemy 1
dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('Brrlgrh... rgrhl... brains...')
dave.set_weakness('cheese')
dining_hall.set_character(dave)

#Creating and setting the enemy 2
dorian = Enemy('Dorian', 'A dark shadow')
dorian.set_conversation('Mmmmuaa...hahahahaa...')
dorian.set_weakness('candle')
kitchen.set_character(dorian)

#Creating and setting the friend
susan = Friend('Susan', 'A gently and beatiful woman caught by Dave')
susan.set_conversation('You need to defeat the enemies first!')
susan.set_gift('kiss')
ballroom.set_character(susan)

#Creating items
cheese = Item('cheese')
candle = Item('candle')
flower = Item('flower')

#Setting items descriptions
cheese.description = 'A blue piece of cheese'
candle.description = 'A magic lit candle'
flower.description = 'A withered flower'

#Setting items in rooms
kitchen.set_item(flower)
dining_hall.set_item(candle)
ballroom.set_item(cheese)

#Creates a RPGInfo object. A new instance called spooky_castle.
spooky_castle = RPGInfo('THE SPOOKY CASTLE')
spooky_castle.welcome()
RPGInfo.rooms = str(Room.number_of_rooms)
RPGInfo.author = "Andres Martinez"
RPGInfo.info()
RPGInfo.game_goal()

#Game
current_room = kitchen
reply = None
command = None
flag =  True
backpack = []
enemies = 0

while flag == True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if inhabitant is not None:
        inhabitant.describe()
    if item is not None:
        item.item_details()
    command = input("> ")
    if command in ['north', 'south', 'east', 'west']:
        current_room = current_room.move(command)
    elif command == 'talk':
        while reply != 'ok':
            inhabitant.talk()
            reply = input("> ")
            if inhabitant == susan and enemies == Enemy.number_of_enemies and reply == 'ok':
                inhabitant.get_gift()
                print(inhabitant.name + ' gives you ' + 'a kiss and leaves the castle.')
                ballroom.set_character(None)
                flag = False
        reply = None
    elif command == 'take':
        item_name = item.name
        backpack.append(item_name)
        current_room.set_item(None)
        lenght = len(backpack)
        print("A [" + backpack[lenght-1] + "] is in your backpack")
    elif command == 'fight' and inhabitant != susan:
        combat_item = inhabitant.fight()
        if backpack == []:
            print("You have nothing in your backpack")
            combat_item = None
        else:
            print("Items available: " + str(backpack))
            for item in backpack:
                if combat_item == item:
                    print("A [" + item + "] has been chosen from your backpack")
                    backpack.remove(item)
                    stock = 1
                else:
                    stock = 0
        if stock == 0:
            print("You don't have that item in your backpack")
            result = inhabitant.check_result(combat_item)
        else:
            result = inhabitant.check_result(combat_item)
        if result == True:
            current_room.set_character(None)
            enemies = enemies + 1
            if enemies == Enemy.number_of_enemies:
                print('You are a hero!')
                susan.set_conversation('You saved me! Do you want a gift?')
        else:
            RPGInfo.game_over()
            flag = False

RPGInfo.credits()